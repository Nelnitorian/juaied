import sys

sys.path.append('/home/edurubcam/workspace/juaied/DAO/')

from userDao import userDao

from tkinter import *
from tkinter import messagebox
from UserPage import UserPage


#Función que checkea username y pass.
def checkAuth(window, username, password):
    
    access = userDao()

    realpassword = access.select_pass(username)

    if (password == realpassword):
        validAuth(window)
    else:
        messagebox.showwarning("Warning", "Usuario y/o contraseña incorrectos")

#Función que lanza la ventana MainPage y cierra AuthenticationPage
def validAuth(window):
    #Cierra la ventana principal
    window.withdraw()

    #Abre MainPage
    window = Tk()
    application = UserPage(window)
    window.mainloop()