from DaoAdmin import DaoAdmin

#Función que checkea username y pass.
def checkAuth(self):
    
    access = DaoAdmin()

    realpassword = access.select_pass(self.username.get())

    if (self.password.get() == realpassword):
        return True
    else:
        return False


def checkNewUser(self):
    
    correct = True

    if(self.apellidos.get() == ''):
        correct = False
    elif(self.nombre.get() == ''):
        correct = False
    elif(self.tarifa.get() == ''):
        correct = False
    elif(self.username.get() == ''):
        correct = False
    elif(self.password.get() == ''):
        correct = False
    
    return correct

def checkModUser(self):
    
    correct = True

    if(self.tarifa.get() == ''):
        correct = False
    elif(self.username.get() == ''):
        correct = False
    elif(self.password.get() == ''):
        correct = False
    
    return correct