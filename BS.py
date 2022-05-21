# -*- coding: utf-8 -*-

from src import loggerConf
from time import sleep
import DaoRad, DaoUserInf, DaoTax

"""

    COMENTARIO SOBRE COSAS QUE CAMBIAR:
        1. Los DAOs que lleven en el constructor a qué IP conectarse.

"""

INTERVAL = 5 #seconds
global STOP_THREADS
global logger, handler, dr, dui, dt


def run():
    global logger, handler, dr, dui
    logger,handler = loggerConf.configureLogger()
    logger.debug('Logger initiated')
    
    dr = DaoRad()
    dui = DaoUserInf()
    dt = DaoTax()
    
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
    global dr
    dic = {}
    for user in usernames:
        time = dr.select_tiempo(user)
        pkg_in = dr.select_paquetes_in(user)
        pkg_out = dr.select_paquetes_out(user)
        pkg_tot = pkg_in + pkg_out
        dic[user] = [time,pkg_tot]
    
    return dic

def updateDatabase(user,data):
    global dui
    time = data[0]
    pkg = data[1]
    dinero = getUpdatedDinero(user,time,pkg)
    dui.update_dinero(user,dinero)
    dui.update_paquetes(user,pkg)
    dui.update_tiempo(user,time)

def getUpdatedDinero(user,time,pkg):
    global dui, dt
    tarifa = dui.select_tarifa(user)
    #TODO modificar para los daos oportunos
    ratio = dt.select_ratio(tarifa)
    control = dt.select_control(tarifa)
    accounted = 0
    if control == 'paquetes':
        accounted = pkg
    else: #control == 'tiempo'
        accounted = time
    dinero = ratio * accounted
    return dinero

if __name__ == '__main__':
    run()
    