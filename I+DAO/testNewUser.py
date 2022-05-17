from tkinter import *

from PageModUser import PageModUser

if __name__ == '__main__':

    window = Tk()
    parent = Tk()
    PageModUser(parent,window)
    window.mainloop()