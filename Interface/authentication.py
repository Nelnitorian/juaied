from tkinter import ttk
from tkinter import *
from checkAuth import checkAuth

class Authentication:
    def __init__(self,window):
        self.wind = window
        self.wind.title('Administration App')

        # Frame container
        frame = LabelFrame(self.wind, text = 'Login')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        #Username Input
        Label(frame, text = 'Username: ').grid(row = 1, column = 0, pady = 5, padx = 5)
        self.username = Entry(frame)
        self.username.grid(row =1, column = 1, padx = 5)
        self.username.focus()

        #Password Input
        Label(frame, text = 'Password: ').grid(row=2,column=0, pady = 5, padx = 5)
        self.password = Entry(frame)
        self.password.grid(row=2,column=1, padx = 5)

        #Button Submit
        button = ttk.Button(frame, text = 'Submit', command=lambda: checkAuth(self.username.get(), self.password.get()))
        button.grid(row=4,columnspan=2,sticky=W+E, pady = 5, padx = 5)


if __name__ == '__main__':
    window = Tk()
    application = Authentication(window)
    window.mainloop()
