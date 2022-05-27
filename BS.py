# -*- coding: utf-8 -*-

from src import loggerConf
from time import sleep
from DAO import DaoRad, DaoUserInf, DaoTax
import sys
import signal

"""

    COMENTARIO SOBRE COSAS QUE CAMBIAR:
        1. Los DAOs que lleven en el constructor a qué IP conectarse.

"""

INTERVAL = 10 #seconds
global logger, handler, dr, dui, dt


def run():
    global logger, handler, dr, dui, dt
    logger,handler = loggerConf.configureLogger()
    logger.debug('Logger initiated')

    dr = DaoRad.DaoRad()
    dui = DaoUserInf.DaoUserInf()
    dt = DaoTax.DaoTax()

    logger.debug('Configuring Ctrl+C handler')
    signal.signal(signal.SIGINT, forceClose)

    nloop=0
    while True:
        logger.debug('Starting loop nº {n}'.format(n=nloop))
        usernames = getUsernames()
        dic = getRemoteData(usernames)
        for user, data in dic.items():
            updateDatabase(user,data)
        nloop+=1
        sleep(INTERVAL)

def getUsernames():
    global dr
    usernames = dr.select_users()
    return usernames

def getRemoteData(usernames):
    global dr
    dic = {}
    for usera in usernames:
        user=usera[0]
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
    logger.debug('Actualización de datos en tabla: user = {user}, time = {time}, pkg = {pkg}'.format(user=user,time=time,pkg=pkg))
    dui.update_dinero(user,dinero)
    dui.update_paquetes(user,pkg)
    dui.update_tiempo(user,time)

def getUpdatedDinero(user,time,pkg):
    global dui, dt
    tarifa = dui.select_tarifa(user)
    ratio = dt.select_ratio(tarifa)
    control = dt.select_control(tarifa)
    accounted = 0
    if control == 'paquetes':
        accounted = pkg
    else: #control == 'tiempo'
        accounted = time
    dinero = ratio * accounted
    return dinero

def forceClose(sig, frame):
    global logger,handler
    logger.debug('Pressed Ctrl+C, closing program!')
    loggerConf.removeLogger(logger,handler)
    sys.exit(0)

if __name__ == '__main__':
    run()
