from ctypes import sizeof
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from PageGeneric import PageGeneric
from UtilitiesFun import *
from DaoUserInf import DaoUserInf

class PageUserInf(PageGeneric):

    def __init__(self,window,parent):
        
        self.win = window
        self.parent = parent

        #Manejo entre ventanas
        self.win.protocol("WM_DELETE_WINDOW", self.on_closing)

        #Titulo
        self.setTitle('Info and Tax User --- Administration App')

        #Tamaño y posicionamiento
        self.setPosition(1500,500)

        #Funcionalidad SELECCIONAR ELEMENTO
        self.win.bind('<<TreeviewSelect>>',self.select)

        #Rows
        self.rows = self.nrows()   

        #Frame container
        frame1 = LabelFrame(self.win)
        frame1.grid(row = 0, column = 0, rowspan = 3, columnspan = 3, padx = 180 )
 
        #Bienvenida Label
        label = Label(frame1, text = 'INFORMACIÓN Y FACTURACIÓN DE USUARIOS')
        label.grid(row = 1,columnspan=2,sticky=W+E, pady = 7, padx = 5)

        #Frame container
        frame2 = LabelFrame(self.win, text = 'Datos en tiempo real')
        frame2.grid(row = 2, column = 0, rowspan = 3, columnspan = 3, padx = 45, pady = 130 )

        #Table
        self.tree = ttk.Treeview(frame2,selectmode = "browse", height=self.rows, columns=("nombre","username","tarifa","dinero","paquetes","tiempo"))
        self.tree.grid(row = 3, column = 0, rowspan=3)
        self.tree.heading('#0', text = 'Apellidos', anchor = CENTER)
        self.tree.heading('nombre', text = 'Nombre', anchor = CENTER)
        self.tree.heading('username', text = 'Username', anchor = CENTER)
        self.tree.heading('tarifa', text = 'Tarifa', anchor = CENTER)
        self.tree.heading('dinero', text = 'Dinero (euro)', anchor = CENTER)
        self.tree.heading('paquetes', text = 'Bytes', anchor = CENTER)
        self.tree.heading('tiempo', text = 'Tiempo (s)', anchor = CENTER)

        #Refresh data
        self.insert_data()

        #Frame container
        frame3 = LabelFrame(self.win)
        frame3.grid(row = 4, column = 0, rowspan = 3, columnspan = 3, padx = 180 )
 
        #Comentario Label
        label = Label(frame3, text = 'SELECCIONE UN USUARIO PARA GENERAR SU FACTURA')
        label.grid(row = 5,columnspan=2,sticky=W+E, pady = 7, padx = 5)
    
        #Frame container
        frame4 = LabelFrame(self.win)
        frame4.grid(row = 6, column = 0, rowspan = 3, columnspan = 3, padx = 180 )

        #Button Back
        back = ttk.Button(frame4, width = 20, text = 'Back', command = lambda: self.on_closing())
        back.grid(row=7,columnspan=2, pady = 7, padx = 5)
    
    def on_closing(self):
        self.tree.after_cancel(self.id)
        self.parent.deiconify()
        self.win.destroy()

    # Devuelve el numero de filas de la tabla
    def nrows(self):
        dao = DaoUserInf()
        return dao.select_rows()

    #Inserta los datos de la BBDD en la tabla
    def insert_data(self):
        #Borrar datos de la tabla
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)

        #Buscar datos de la tabla en BBDD
        dao = DaoUserInf()

        apellidos = dao.select_users()

        for ap in apellidos:
            a = ap[0]
            user = dao.select_username_by_apellidos(a)
            self.tree.insert("",END,text=a,
                values=(
                    dao.select_nombre(user),
                    user,
                    dao.select_tarifa(user),
                    dao.select_dinero(user),
                    dao.select_paquetes(user),
                    dao.select_tiempo(user)
                    ))

        #Refresar datos cada 3 segundos
        self.id = self.tree.after(3000,self.insert_data)

    def select(self,event):

        #Con "try" solo tenemos en cuenta el evento seleccionar, no el deselecionar
        try:
            username = self.tree.item(self.tree.selection())['values'][1]
            nombre = self.tree.item(self.tree.selection())['values'][0]
            apellidos = self.tree.item(self.tree.selection())['text']
            election = messagebox.askokcancel(message="¿Realizar factura para {} {}?".format(nombre, apellidos), title="Confimar elección")
            
            if(election == True):
                print("Se genera factura")
            else:
                print("No se genera la factura")

        except Exception as e:
            pass

