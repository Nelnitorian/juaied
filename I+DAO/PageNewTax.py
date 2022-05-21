from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from PageGeneric import PageGeneric
from UtilitiesFun import *
from DaoTax import DaoTax

class PageNewTax(PageGeneric):

    def __init__(self,window,parent):
        
        self.win = window
        self.parent = parent

        #Manejo entre ventanas
        self.win.protocol("WM_DELETE_WINDOW", self.on_closing)

        #Titulo
        self.setTitle('New Tax --- Administration App')

        #Tamaño y posicionamiento
        self.setPosition(500,500)

        #Funcionalidad ENTER
        self.win.bind('<Return>',self.asButton)        

        #Frame container
        frame1 = LabelFrame(self.win)
        frame1.grid(row = 0, column = 0, rowspan = 3, columnspan = 3, padx = 180 , pady = 50)
 
        #Bienvenida Label
        label = Label(frame1, text = 'NUEVA TARIFA')
        label.grid(row = 1,columnspan=2,sticky=W+E, pady = 7, padx = 5)

        #Frame container
        frame2 = LabelFrame(self.win, text = 'Introduzca los siguientes datos')
        frame2.grid(row = 6, column = 0, rowspan = 3, columnspan = 3, padx = 45, pady = 0 )

        #Label tarifa
        Label(frame2, text = 'Tarifa: ').grid(row = 7, column = 0, pady = 10, padx = 5)
        self.tarifa = Entry(frame2, width=30)
        self.tarifa.grid(row =7, column = 1, padx = 5)
        self.tarifa.focus()

        #Label control
        Label(frame2, text = 'Control: ').grid(row = 8, column = 0, pady = 7, padx = 5)
        self.control = Entry(frame2, width=30)
        self.control.grid(row =8, column = 1, padx = 5)

        #Label ratio
        Label(frame2, text = 'Ratio: ').grid(row = 9, column = 0, pady = 7, padx = 5)
        self.ratio = Entry(frame2, width=30)
        self.ratio.grid(row =9, column = 1, padx = 5)

        #Frame container
        frame3 = LabelFrame(self.win)
        frame3.grid(row = 10, column = 0, rowspan = 3, columnspan = 3, padx = 45, pady = 30)

        #Button Submit
        button = ttk.Button(frame3, width = 20, text = 'Submit', command = lambda: self.asButton(event='<Return>'))
        button.grid(row=10, column = 0, pady = 7)

        #Button Back
        back = ttk.Button(frame3, width = 20, text = 'Back', command = lambda: self.on_closing())
        back.grid(row=10, column=1, pady = 7)

    def asButton(self,event):
        if(checkNewTax(self)):
            if(self.persist_tax()):
                messagebox.showinfo("Info","Nueva tarifa agregada correctamente")

                #Borramos datos del formulario
                self.delete_form()

            else:
                messagebox.showerror("Error","Ha ocurrido un error al guardar la tarifa en BBDD")
        else:
            messagebox.showwarning("Warning", "Falta algún dato por introducir")

    def on_closing(self):
         self.parent.deiconify()
         self.win.destroy()
    
    def delete_form(self):
        self.tarifa.delete("0","end")
        self.control.delete("0","end")
        self.ratio.delete("0","end")

    def persist_tax(self):
        daotax = DaoTax()

        daotax.new_tarifa(self.tarifa.get(),self.control.get(),self.ratio.get())

        return True
