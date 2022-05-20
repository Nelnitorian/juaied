# -*- coding: utf-8 -*-

from src import loggerConf
from time import sleep
import DaoRad, DaoUserInf

"""

    COMENTARIO SOBRE COSAS QUE CAMBIAR:
        1. Los DAOs que lleven en el constructor a qué IP conectarse.

"""

INTERVAL = 5 #seconds
global STOP_THREADS
global logger
global handler

def runDatabase():
    #TODO Iniciar la base de datos, no sé cómo hacerlo (de momento)
    pass

def run():
    global logger, handler
    logger,handler = loggerConf.configureLogger()
    logger.debug('Logger initiated')
    
    while True:
        usernames = getUsernames()
        dic = getRemoteData(usernames)
        for user, data in dic.items():
            updateDatabase(user,data)
        
        sleep(INTERVAL)
        
def getUsernames():
    #TODO Hay que encontrar la lista de los usuarios.
    usernames = ['usertest']
    return usernames

def getRemoteData(usernames):
    
    dic = {}
    for user in usernames:
        time = DaoRad.select_tiempo(user)
        pkg_in = DaoRad.select_paquetes_in(user)
        pkg_out = DaoRad.select_paquetes_out(user)
        pkg_tot = pkg_in + pkg_out
        dic[user] = [time,pkg_tot]
    
    return dic

def updateDatabase(user,data):
    time = data[0]
    pkg = data[1]
    DaoUserInf.update_paquetes(user,pkg)
    DaoUserInf.update_tiempo(user,time)


if __name__ == '__main__':
    runDatabase()
    run()
    