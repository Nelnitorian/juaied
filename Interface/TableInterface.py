from tkinter import ttk
from tkinter import *

#Tabla de 10 filas y 2 columnas
self.tree = ttk.Treeview(height=10,columns=2)

#Posicionamiento de la tabla
self.tree.grid()

#Titulo
self.tree.heading('#0', text = 'Name', anchor = CENTER)
self.tree.heading('#1', text = 'Price', anchor = CENTER)
