import sys
sys.path.append('/home/edurubcam/workspace/juaied/DAO/')

from userDao import userDao

def checkAuth(username, password):
    
    access = userDao()

    realpassword = access.select_pass(username)

    if (password == realpassword):
        print("Authentication correct")
    else:
        print("Authentication incorrect")