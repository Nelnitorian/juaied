from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from PageGeneric import PageGeneric
from UtilitiesFun import *
from DaoModUser import DaoModUser
from DaoNewRadUser import DaoNewRadUser

class PageModUser(PageGeneric):

    def __init__(self,window,parent):
        
        self.win = window
        self.parent = parent

        self.usuarios = self.buscaUsuarios()

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
        frame1.grid(row = 0, column = 0, rowspan = 3, columnspan = 3, padx = 180,pady=20 )
 
        #Bienvenida Label
        label = Label(frame1, text = 'MODIFICAR USUARIO')
        label.grid(row = 1,columnspan=2,sticky=W+E, pady = 7, padx = 5)

        #Frame container
        frame2 = LabelFrame(self.win, text = 'Seleccione usuario')
        frame2.grid(row = 2, column = 0, rowspan = 3, columnspan = 3, padx = 45, pady = 0 )

        #Label Apellidos, Nombre
        Label(frame2, text = 'Apellidos: ').grid(row = 3, column = 0, pady = 10, padx = 5)
        self.combo = ttk.Combobox(frame2, state="readonly",values=self.usuarios)
        self.combo.grid(row =3, column = 1, padx = 5)
        self.combo.bind("<<ComboboxSelected>>", self.selection_changed)

        #Frame continer
        frame3 = LabelFrame(self.win, text = 'Puede modificar los siguientes datos')
        frame3.grid(row = 4, column = 0, rowspan = 3, columnspan = 3, padx = 45, pady = 120)

        #Label Tarifa
        Label(frame3, text = 'Tarifa: ').grid(row = 5, column = 0, pady = 7, padx = 5)
        self.tarifa = Entry(frame3, width=30)
        self.tarifa.grid(row =5, column = 1, padx = 5)
        #TODO SELECT OPTIONS

        #Label username
        Label(frame3, text = 'UserName: ').grid(row = 6, column = 0, pady = 7, padx = 5)
        self.username = Entry(frame3, width=30)
        self.username.grid(row =6, column = 1, padx = 5)

        #Label password
        Label(frame3, text = 'Password: ').grid(row = 7, column = 0, pady = 7, padx = 5)
        self.password = Entry(frame3, width=30)
        self.password.grid(row =7, column = 1, padx = 5)

        #Button Submit
        button = ttk.Button(frame3, width = 20, text = 'Submit', command = lambda: self.asButton(event='<Return>'))
        button.grid(row=8,columnspan=2, pady = 7, padx = 5)
    

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
        dao = DaoModUser()
        users = dao.select_users()
        userArray = []
        for user in users:
          userArray.append("{}".format(user[0]))
        return userArray

    def selection_changed(self,event):
        self.apellidos = self.combo.get()
        dao = DaoModUser()
        info = dao.select_user_information(self.apellidos)
        self.tarifa.insert(0,info[0])
        self.username.insert(0,info[1])
        self.oldusername = info[1]
        self.password.insert(0,info[2])

    def updateInfo(self):
        radDao = DaoNewRadUser()
        radDao.update_user(self.username.get(),self.password.get(),self.oldusername)

        userDao = DaoModUser()
        userDao.update_user_data(self.username.get(),self.password.get(),self.tarifa.get(),self.apellidos)

        return True
        