from tkinter import *
from tkinter import ttk
from turtle import window_height

class UserPage:
    def __init__(self,window):
        self.wind = window

        #Title
        self.wind.title('Administration App')

        #Posicionamineto
        self.x = (window.winfo_screenwidth()//2) - (window.winfo_width()//2)
        self.y = (window.winfo_screenheight()//2) - (window.winfo_height()//2)
        self.wind.geometry('{}x{}+{}+{}'.format(680,500,self.x-340,self.y-300))

        #Color background
        #self.wind.configure(background='white')

        # Frame container
        frame = LabelFrame(self.wind, text = 'DATA')
        frame.grid(row = 0, column = 0, rowspan = 3, columnspan = 3, pady = 60, padx = 100 )
