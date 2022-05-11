from tkinter import *
from tkinter import ttk

class PageGeneric(object):

    def setTitle(self, title):
        self.win.title(title)

    def setPosition(self,fx,fy):
        x = (self.win.winfo_screenwidth()//2) - (self.win.winfo_width()//2)
        y = (self.win.winfo_screenheight()//2) - (self.win.winfo_height()//2)
        self.win.geometry('{}x{}+{}+{}'.format(fx,fy,x-fx//2,y-fy//2-100))

    def setBackgroundColour(self,color):
        self.win.configure(background=color)
