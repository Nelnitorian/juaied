from tkinter import *
from tkinter import ttk
from turtle import window_height
from loginfunct import checkAuth

class AuthenticationPage:
    def __init__(self,window):
        self.wind = window

        #Title
        self.wind.title('Administration App')

        #Posicionamineto
        self.x = (window.winfo_screenwidth()//2) - (window.winfo_width()//2)
        self.y = (window.winfo_screenheight()//2) - (window.winfo_height()//2)
        self.wind.geometry('{}x{}+{}+{}'.format(480,300,self.x-240,self.y-250))

        #Color background
        #self.wind.configure(background='white')

        # Frame container
        frame = LabelFrame(self.wind, text = 'Login')
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
        button = ttk.Button(frame, text = 'Submit', command=lambda: checkAuth(self.wind,self.username.get(), self.password.get()))
        button.grid(row=4,columnspan=2,sticky=W+E, pady = 5, padx = 5)

        #ENTER as Button
        def asButton(event):
            checkAuth(self.wind,self.username.get(), self.password.get())

        self.wind.bind('<Return>',asButton)
