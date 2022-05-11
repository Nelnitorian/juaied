from tkinter import *
from tkinter import ttk
from PageGeneric import PageGeneric

class PageUser(PageGeneric):

    def __init__(self,window):
        
        self.win = window

        #Titulo
        self.setTitle('Main --- Administration App')

        #Tamaño y posicionamiento
        self.setPosition(500,400)

        #Funcionalidad ENTER
        #self.win.bind('<Return>',self.asButton)        

        #Frame container
        frame1 = LabelFrame(self.win)
        frame1.grid(row = 0, column = 0, rowspan = 3, columnspan = 3, padx = 100 )
 
        #Bienvenida Label
        label = Label(frame1, text = 'BIENVENIDO, ADMINISTRADOR DE LA RED.')
        label.grid(row = 1,columnspan=2,sticky=W+E, pady = 7, padx = 5)

        #Frame container
        frame2 = LabelFrame(self.win, text = 'Opciones')
        frame2.grid(row = 2, column = 0, rowspan = 3, columnspan = 3, pady = 100, padx = 100 )
        
        #Informacion de usuario Button
        button1 = ttk.Button(frame2, text = 'INFORMACIÓN DE USUARIOS', command=lambda: self.userList(self.win))
        button1.grid(row=3,columnspan=2,sticky=W+E, pady = 7, padx = 5)

        #Crear Tarifa Button
        button2 = ttk.Button(frame2, text = 'NUEVA TARIFA', command=lambda: self.newCharge(self.win))
        button2.grid(row=4,columnspan=2,sticky=W+E, pady = 7, padx = 5)

        #Nuevo Usuario Button
        button3 = ttk.Button(frame2, text = 'NUEVO USUARIO', command=lambda: self.newUser(self.win))
        button3.grid(row=5,columnspan=2,sticky=W+E, pady = 7, padx = 5)

        #Modificar Usuario Button
        button3 = ttk.Button(frame2, text = 'MODIFICAR USUARIO', command=lambda: self.updateCharge(self.win))
        button3.grid(row=6,columnspan=2,sticky=W+E, pady = 7, padx = 5)

        #LogOut Button
        buttonLO = ttk.Button(self.win, text = 'LogOut', command= lambda: self.logOut(self.win))
        buttonLO.place(x=500,y=400, anchor='se')

    def userList(self):
        pass

    def newCharge(self):
        pass

    def newUser(self):
        pass

    def updateUser(self):
        pass

    def logOut(self):
        pass