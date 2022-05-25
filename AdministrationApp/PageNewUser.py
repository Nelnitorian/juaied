from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from PageGeneric import PageGeneric
from UtilitiesFun import *
from DaoRad import DaoRad
from DaoUserInf import DaoUserInf
from DaoTax import DaoTax

class PageNewUser(PageGeneric):

    def __init__(self,window,parent):
        
        self.win = window
        self.parent = parent

        self.tarifas = self.buscaTarifas()

        #Manejo entre ventanas
        self.win.protocol("WM_DELETE_WINDOW", self.on_closing)

        #Titulo
        self.setTitle('New User --- Administration App')

        #Tamaño y posicionamiento
        self.setPosition(500,500)

        #Funcionalidad ENTER
        self.win.bind('<Return>',self.asButton)        

        #Frame container
        frame1 = LabelFrame(self.win)
        frame1.grid(row = 0, column = 0, rowspan = 3, columnspan = 3, padx = 180, pady=50 )
 
        #Bienvenida Label
        label = Label(frame1, text = 'NUEVO USUARIO')
        label.grid(row = 1,columnspan=2,sticky=W+E, pady = 7, padx = 5)

        #Frame container
        frame2 = LabelFrame(self.win, text = 'Introduzca los siguientes datos')
        frame2.grid(row = 5, column = 0, rowspan = 3, columnspan = 3, padx = 45, pady = 0 )

        #Label Apellidos
        Label(frame2, text = 'Apellidos: ').grid(row = 6, column = 0, pady = 10, padx = 5)
        self.apellidos = Entry(frame2, width=30)
        self.apellidos.grid(row =6, column = 1, padx = 5)
        self.apellidos.focus()

        #Label Nombre
        Label(frame2, text = 'Nombre: ').grid(row = 7, column = 0, pady = 7, padx = 5)
        self.nombre = Entry(frame2, width=30)
        self.nombre.grid(row =7, column = 1, padx = 5)

        #Label Tarifa
        Label(frame2, text = 'Tarifa: ').grid(row = 8, column = 0, pady = 7, padx = 5)
        self.tarifa = ttk.Combobox(frame2, state="readonly",values=self.tarifas)
        self.tarifa.grid(row =8, column = 1, padx = 5)
                
        #Label username
        Label(frame2, text = 'UserName: ').grid(row = 9, column = 0, pady = 7, padx = 5)
        self.username = Entry(frame2, width=30)
        self.username.grid(row =9, column = 1, padx = 5)

        #Label password
        Label(frame2, text = 'Password: ').grid(row = 10, column = 0, pady = 7, padx = 5)
        self.password = Entry(frame2, width=30)
        self.password.grid(row =10, column = 1, padx = 5)

        #Frame container
        frame3 = LabelFrame(self.win)
        frame3.grid(row = 11, column = 0, rowspan = 3, columnspan = 3, padx = 45, pady = 30)

        #Button Submit
        button = ttk.Button(frame3, width = 20, text = 'Submit', command = lambda: self.asButton(event='<Return>'))
        button.grid(row=12, column = 0, pady = 7)

        #Button Back
        back = ttk.Button(frame3, width = 20, text = 'Back', command = lambda: self.on_closing())
        back.grid(row=12,column = 1, pady = 7)
    

    def asButton(self,event):
        if(checkNewUser(self)):
            if(self.persist_user()):
                messagebox.showinfo("Info","Nuevo usuario agregado correctamente")

                #Borramos datos del formulario
                self.delete_form()

            else:
                messagebox.showerror("Error","Ha ocurrido un error al guardar el usuario en BBDD")
        else:
            messagebox.showwarning("Warning", "Falta algún dato por introducir")

    def on_closing(self):
         self.parent.deiconify()
         self.win.destroy()
    
    def delete_form(self):
        self.apellidos.delete("0","end")
        self.nombre.delete("0","end")

        self.username.delete("0","end")
        self.password.delete("0","end")

    def persist_user(self):
        daorad = DaoRad()
        daouser = DaoUserInf()

        daorad.add_user(self.username.get(),self.password.get())

        daouser.new_user(self.username.get(),self.password.get(),self.apellidos.get(),self.nombre.get(),self.tarifa.get())

        return True

    def buscaTarifas(self):
        dao = DaoTax()
        tarifas = dao.select_tarifas()
        tarifaArray = []
        for tarifa in tarifas:
          tarifaArray.append("{}".format(tarifa[0]))
        return tarifaArray