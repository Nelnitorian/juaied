from tkinter import *
from tkinter import messagebox


from DaoAdmin import DaoAdmin
from PageUser import PageUser


#Función que checkea username y pass.
def checkAuth(window, username, password):
    
    access = DaoAdmin()

    realpassword = access.select_pass(username)

    if (password == realpassword):
        validAuth(window)
    else:
        messagebox.showwarning("Warning", "Usuario y/o contraseña incorrectos")

#Función que lanza la ventana MainPage y cierra AuthenticationPage
def validAuth(window):
    #Cierra la ventana principal
    window.destroy()

    #Abre MainPage
    window = Tk()
    PageUser(window)
    window.mainloop()