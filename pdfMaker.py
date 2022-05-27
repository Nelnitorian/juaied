# -*- coding: utf-8 -*-

#import sys; print(sys.version)
#Main imports
from borb.pdf import Document
from borb.pdf.page.page import Page
# New import
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from decimal import Decimal
# New import
from borb.pdf.canvas.layout.image.image import Image


# New imports
from borb.pdf.canvas.layout.table.fixed_column_width_table import FixedColumnWidthTable as Table
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.canvas.layout.layout_element import Alignment
from datetime import datetime
import random

# New imports
from borb.pdf.canvas.color.color import HexColor, X11Color

# New import
from borb.pdf.canvas.layout.table.fixed_column_width_table import FixedColumnWidthTable as Table
from borb.pdf.canvas.layout.table.table import TableCell


# New import
from borb.pdf.pdf import PDF

from src import loggerConf
from DAO import DaoTax

import os


class PdfMaker():

    def __init__(self, username, apellidos, nombre, tarifa, dinero, paquetes, tiempo, logger):
        logger.debug("Initiating PdfMaker...")

        self.dt = DaoTax.DaoTax()

        self.logger = logger

        self.username = username
        self.name = nombre
        self.surname = apellidos
        self.tarifa = tarifa

        self.time = tiempo
        self.paquetes = paquetes
        self.uprice = self.dt.select_ratio(tarifa)
        self.money = dinero
        self.monitor = self.dt.select_control(tarifa)



        #Create document
        self.pdf = Document()

        # Add page
        self.page = Page()
        self.pdf.append_page(self.page)

        self.page_layout = SingleColumnLayout(self.page)
        self.page_layout.vertical_margin = self.page.get_page_info().get_height() * Decimal(0.02)


        self.page_layout.add(
                Image(
                "https://drive.google.com/uc?id=1H-9_qsGueIgMVjmrR8GX2rxkBl-eMePC",
                width=Decimal(128*1.8),
                height=Decimal(128),
                ))


        # Invoice information table
        self.page_layout.add(self._build_invoice_information())

        # Empty paragraph for spacing
        self.page_layout.add(Paragraph(" "))

        # Billing and shipping information table
        self.page_layout.add(self._build_billing_and_shipping_information())

        # Empty paragraph for spacing
        self.page_layout.add(Paragraph(" "))

        # Itemized description
        self.page_layout.add(self._build_itemized_description_table())

        logger.debug("Finished initiating PdfMaker.")

    def _build_invoice_information(self):

        table_001 = Table(number_of_rows=4, number_of_columns=2)


        table_001.add(Paragraph("Date", font="Helvetica-Bold"))
        now = datetime.now()
        table_001.add(Paragraph("%d/%d/%d" % (now.day, now.month, now.year)))

        table_001.add(Paragraph("Invoice #", font="Helvetica-Bold"))
        table_001.add(Paragraph("%d" % random.randint(1000, 10000)))

        table_001.add(Paragraph("Due Date", font="Helvetica-Bold"))
        table_001.add(Paragraph("%d/%d/%d" % (now.day, now.month, now.year)))

        table_001.add(Paragraph("Company", font="Helvetica-Bold"))
        table_001.add(Paragraph("Juaied"))

        table_001.set_padding_on_all_cells(Decimal(2), Decimal(2), Decimal(2), Decimal(2))
        table_001.no_borders()

        return table_001


    def _build_billing_and_shipping_information(self):
        table_001 = Table(number_of_rows=4, number_of_columns=1)
        table_001.add(
            Paragraph(
                "BILL TO",
                background_color=HexColor("263238"),
                font_color=X11Color("White"),
            )
        )
        table_001.add(Paragraph('{surname}, {name}'.format(surname=self.surname,name=self.name)))        # BILLING
        table_001.add(Paragraph("{u}".format(u=self.username)))  # BILLING
        table_001.add(Paragraph("{t}".format(t=self.tarifa)))    # BILLING
        table_001.set_padding_on_all_cells(Decimal(2), Decimal(2), Decimal(2), Decimal(2))
        table_001.no_borders()
        return table_001


    def _build_itemized_description_table(self):
        table_001 = Table(number_of_rows=9, number_of_columns=4)
        for h in ["DESCRIPTION", "QTY", "UNIT PRICE", "AMOUNT"]:
            table_001.add(
                TableCell(
                    Paragraph(h, font_color=X11Color("White")),
                    background_color=HexColor("016934"),
                )
            )

        odd_color = HexColor("BBBBBB")
        even_color = HexColor("FFFFFF")
        total_money = 0

        if self.monitor == 'paquetes':
            self.qty = self.paquetes
        else:
            self.qty = self.time

        for row_number, item in enumerate([(self.monitor, self.qty, self.uprice, self.money)]):
            c = even_color if row_number % 2 == 0 else odd_color
            table_001.add(TableCell(Paragraph(item[0]), background_color=c))
            table_001.add(TableCell(Paragraph(str(item[1])), background_color=c))
            table_001.add(TableCell(Paragraph("$ " + str(item[2])), background_color=c))
            table_001.add(TableCell(Paragraph("$ " + str(item[3])), background_color=c))
            total_money += item[3]

    	# Optionally add some empty rows to have a fixed number of rows for styling purposes
        for row_number in range(1, 4):
            c = even_color if row_number % 2 == 0 else odd_color
            for _ in range(0, 4):
                table_001.add(TableCell(Paragraph(" "), background_color=c))

        table_001.add(TableCell(Paragraph("Subtotal", font="Helvetica-Bold", horizontal_alignment=Alignment.RIGHT,), col_span=3,))
        table_001.add(TableCell(Paragraph("$ {tm:.2f}".format(tm=total_money/1.1), horizontal_alignment=Alignment.RIGHT)))
        table_001.add(TableCell(Paragraph("Discounts", font="Helvetica-Bold", horizontal_alignment=Alignment.RIGHT,),col_span=3,))
        table_001.add(TableCell(Paragraph("$ {d:.2f}".format(d=0.0), horizontal_alignment=Alignment.RIGHT)))
        table_001.add(TableCell(Paragraph("Taxes", font="Helvetica-Bold", horizontal_alignment=Alignment.RIGHT), col_span=3,))
        table_001.add(TableCell(Paragraph("$ {t:.2f}".format(t=total_money*0.1/1.1), horizontal_alignment=Alignment.RIGHT)))
        table_001.add(TableCell(Paragraph("Total", font="Helvetica-Bold", horizontal_alignment=Alignment.RIGHT  ), col_span=3,))
        table_001.add(TableCell(Paragraph("$ {tm:.2f}".format(tm=total_money), horizontal_alignment=Alignment.RIGHT)))
        table_001.set_padding_on_all_cells(Decimal(2), Decimal(2), Decimal(2), Decimal(2))
        table_001.no_borders()
        return table_001

    def dumpPdf(self):
        folder = 'facturas'
        loggerConf.createFolder(folder)
        pdf_name = '{s}_{n}.pdf'.format(s=self.surname.replace(' ',''),n=self.name.replace(' ',''))
        path = os.path.join(folder,pdf_name)
        with open(path, "wb") as pdf_file_handle:
            PDF.dumps(pdf_file_handle, self.pdf)
            self.logger.debug("PDF dumped properly")


if __name__ == '__main__':

    logger,handler = loggerConf.configureLogger()

    username = "edurubcam"
    nombre = "Eduardo"
    apellidos = "Rubio Camacho"
    tarifa = "default"

    paquetes = 100
    tiempo = 100
    dinero = 13

    pdfmaker = PdfMaker(username, apellidos, nombre, tarifa, dinero, paquetes, tiempo, logger)
    pdfmaker.dumpPdf()

    loggerConf.removeLogger(logger,handler)
