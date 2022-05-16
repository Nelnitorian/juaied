# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""

    Glosario:
        -RSC: Radius server que se porta como cliente al enviar la base de datos al BS
        -BS: Billing server que se porta como servidor al recibir la base de datos enviada por el RSC


"""
from src import loggerConf,protocol
import socket
from time import sleep
from threading import Thread

TCP_IP = 'localhost'
TCP_PORT = 9001
BUFFER_SIZE = 1024
INTERVAL = 10 #seconds
LOGGING_FOLDER = 'log'
global STOP_THREADS
STOP_THREADS = False

def run():
    
    
    logger,handler = loggerConf.configureLogger()
    logger.debug('Logger initiated')
    
    logger.debug('Initiating socket')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    
    
    if login(s):
        
        logger.debug('Login successful')
        #Receiving thread
        logger.debug('Starting receiving thread...')
        receiveThread = Thread(target = receiveFunc,args=(s,logger,))
        try:
            receiveThread.start()
            
            #TODO: este if antes era un while
            if True:
                usernames = fetchUsernames()
                for user in usernames:
                    data = fetchUserData(user)
                    msg = createProtocolMessage(user, data)
                    logger.debug('Sending data {data} to server...'.format(data=msg))
                    #s.send(msg.encode())
                
                sleep(INTERVAL)

        except:
            logger.error('A fatal error ocurred.')
        finally:
            logger.debug('Stopping threads')
            global STOP_THREADS
            STOP_THREADS = True
            
            #TODO comprender comportamiento de Thread, join y try/except
            #receiveThread.join()
            try:
                s.close()
            except:
                print("Error, no hago nada")
            logger.debug('Connection closed')
    logger.debug('Closing logger handler...')
    logger.removeHandler(handler)
    handler.close()
    
def fetchUsernames():
    #TODO
    #Interfaz aún por hacer
    usernames = ["foo"]
    return usernames

def fetchUserData(username):
    #TODO
    #Algo del DAO
    data = 454567
    return data

def createProtocolMessage(username,data):
    #creates message
    msg = protocol.C2Smsg(username,data)
    return msg

def login(s):
    #TODO
    #login, return True if successful
    #https://www.paladion.net/blogs/sending-salted-hashes-just-got#:~:text=Let%27s%20call%20the%20user-specific,is%20Hash(password%2C%20user_salt)
    return True   

def receiveFunc(s,logger):
    global STOP_THREADS
    #TODO este if antes era un while
    if not STOP_THREADS:
        msg = s.recv(BUFFER_SIZE).decode()
        #we may have received more than one msg, we have to separate them
        msgs = protocol.separate(msg)
        for data in msgs:
            username, status = protocol.extract(data)
            logger.debug('Updating {u}\'s status to {s}'.format(u=username,s=status))
            updateStatus(username,status)
    pass
    
def updateStatus(username,status):
    #TODO
    if (status==protocol.LIMIT_REACHED):
        #Generates a CoA Radius Server -> Radius Client https://freeradius-users.freeradius.narkive.com/5mZXm1fD/setup-freeradius-to-generateng-coa
        pass
    return True

if __name__ == '__main__':
    run()
    
    
    
    
    