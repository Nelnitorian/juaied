from tkinter import *
from tkinter import ttk

from PageGeneric import PageGeneric
from UtilitiesFun import *

class PageLogin(PageGeneric):

    def __init__(self,window):
 
        self.win = window

        #Titulo
        self.setTitle('Login --- Administration App')

        #Tamaño y posicionamiento
        self.setPosition(480,300)

        #Funcionalidad ENTER
        self.win.bind('<Return>',self.asButton)

         # Frame container
        frame = LabelFrame(self.win, text = 'Login')
        frame.grid(row = 0, column = 0, rowspan = 3, columnspan = 3, pady = 60, padx = 100 )

        #Username Input
        Label(frame, text = 'Username: ').grid(row = 1, column = 0, pady = 5, padx = 5)
        self.username = Entry(frame)
        self.username.grid(row =1, column = 1, padx = 5)
        self.username.focus()

        #Password Input
        Label(frame, text = 'Password: ').grid(row=2,column=0, pady = 5, padx = 5)
        self.password = Entry(frame, show='*')
        self.password.grid(row=2,column=1, padx = 5)

        #Button Submit
        button = ttk.Button(frame, text = 'Submit', command=lambda: checkAuth(self.win,self.username.get(), self.password.get()))
        button.grid(row=4,columnspan=2,sticky=W+E, pady = 5, padx = 5)

    def asButton(self,event):
        checkAuth(self.win,self.username.get(), self.password.get())