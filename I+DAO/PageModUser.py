from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from PageGeneric import PageGeneric
from UtilitiesFun import *
from DaoUserInf import DaoUserInf
from DaoRad import DaoRad
from DaoTax import DaoTax

class PageModUser(PageGeneric):

    def __init__(self,window,parent):
        
        self.win = window
        self.parent = parent

        #Usuarios registrados
        self.usuarios = self.buscaUsuarios()

        #Tarifas registradas
        self.tarifas = self.buscaTarifas()

        #Manejo entre ventanas
        self.win.protocol("WM_DELETE_WINDOW", self.on_closing)

        #Titulo
        self.setTitle('Mod User --- Administration App')

        #Tamaño y posicionamiento
        self.setPosition(500,500)

        #Funcionalidad ENTER
        self.win.bind('<Return>',self.asButton)        

        #Frame container
        frame1 = LabelFrame(self.win)
        frame1.grid(row = 0, column = 0, rowspan = 3, columnspan = 3, padx = 180,pady=50 )
 
        #Bienvenida Label
        label = Label(frame1, text = 'MODIFICAR USUARIO')
        label.grid(row = 1,columnspan=2,sticky=W+E, pady = 7, padx = 5)

        #Frame container
        frame2 = LabelFrame(self.win, text = 'Seleccione usuario')
        frame2.grid(row = 4, column = 0, rowspan = 3, columnspan = 3, padx = 45, pady = 0)

        #Label Apellidos, Nombre
        Label(frame2, text = 'Apellidos: ').grid(row = 5, column = 0, pady = 10, padx = 5)
        self.combo = ttk.Combobox(frame2, state="readonly",values=self.usuarios)
        self.combo.grid(row =5, column = 1, padx = 5)
        self.combo.bind("<<ComboboxSelected>>", self.selection_changed)

        #Frame continer
        frame3 = LabelFrame(self.win, text = 'Puede modificar los siguientes datos')
        frame3.grid(row = 8, column = 0, rowspan = 3, columnspan = 3, padx = 45, pady = 20)

        #Label Tarifa
        Label(frame3, text = 'Tarifa: ').grid(row = 9, column = 0, pady = 7, padx = 5)
        self.tarifa = ttk.Combobox(frame3, state="readonly",values=self.tarifas)
        self.tarifa.grid(row =9, column = 1, padx = 5)

        #Label username
        Label(frame3, text = 'UserName: ').grid(row = 10, column = 0, pady = 7, padx = 5)
        self.username = Entry(frame3, width=30)
        self.username.grid(row =10, column = 1, padx = 5)

        #Label password
        Label(frame3, text = 'Password: ').grid(row = 11, column = 0, pady = 7, padx = 5)
        self.password = Entry(frame3, width=30)
        self.password.grid(row =11, column = 1, padx = 5)

        #Frame container
        frame4 = LabelFrame(self.win)
        frame4.grid(row = 12, column = 0, rowspan = 3, columnspan = 3, padx = 45, pady = 0)

        #Button Submit
        button = ttk.Button(frame4, width = 20, text = 'Submit', command = lambda: self.asButton(event='<Return>'))
        button.grid(row=13, column = 0, pady = 7)

        #Button Back
        back = ttk.Button(frame4, width = 20, text = 'Back', command = lambda: self.on_closing())
        back.grid(row=13, column=1, pady = 7)    

    def asButton(self,event):
        if(checkModUser(self)):
            if(self.updateInfo()):

                messagebox.showinfo("Info","Usuario modificado correctamente")

            else:
                messagebox.showerror("Error","Ha ocurrido un error al guardar el usuario en BBDD")
        else:
            messagebox.showwarning("Warning", "Falta algún dato por introducir")

    def on_closing(self):
         self.parent.deiconify()
         self.win.destroy()

    def buscaUsuarios(self):
        dao = DaoUserInf()
        users = dao.select_users()
        userArray = []
        for user in users:
          userArray.append("{}".format(user[0]))
        return userArray

    def selection_changed(self,event):
        
        self.apellidos = self.combo.get()
        dao = DaoUserInf()
        username = dao.select_username_by_apellidos(self.apellidos)
        self.oldusername = username
        #info = dao.select_user_information(self.apellidos)

        #Actualizamos datos
        self.username.delete(0,"end")
        self.password.delete(0,"end")
        self.tarifa.set(dao.select_tarifa(username))
        self.username.insert(0,username)
        self.password.insert(0,dao.select_pass(username))

    def updateInfo(self):
        radDao = DaoRad()
        radDao.update_user(self.username.get(),self.password.get(),self.oldusername)

        userDao = DaoUserInf()
        
        userDao.update_username(self.oldusername, self.username.get())
        userDao.update_pass(self.username.get(),self.password.get())
        userDao.update_tarifa(self.username.get(),self.tarifa.get())

        return True

    def buscaTarifas(self):
        dao = DaoTax()
        tarifas = dao.select_tarifas()
        tarifaArray = []
        for tarifa in tarifas:
          tarifaArray.append("{}".format(tarifa[0]))
        return tarifaArray
        