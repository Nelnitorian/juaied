# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""

    Glosario:
        -RSC: Radius server que se porta como cliente al enviar la base de datos al BS
        -BS: Billing server que se porta como servidor al recibir la base de datos enviada por el RSC


"""

import protocol, loggerConf
import socket
from threading import Thread

TCP_IP = 'localhost'
TCP_PORT = 9001
BUFFER_SIZE = 1024
INTERVAL = 10 #seconds
global STOP_THREADS
STOP_THREADS = False
MAX_SERVERS = 2

def run():
    
    logger,handler = loggerConf.configureLogger()
    
    tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcpsock.bind((TCP_IP, TCP_PORT))
    threads = []
    
    global STOP_THREADS
    while not STOP_THREADS:
        tcpsock.listen(MAX_SERVERS)
        logger.debug("Waiting for incoming connections...")
        (conn, (ip,port)) = tcpsock.accept()
        logger.debug('Got connection from ', (ip,port))
        newthread = Thread(target = _sessionThread,args=(conn,logger,))
        newthread.start()
        threads.append(newthread)
    
    for t in threads:
        t.join()
    logger.debug('Closing logger handler...')
    logger.removeHandler(handler)
    handler.close()

def _sessionThread(s,logger):
    
    if _login(s):
        
        #Receiving thread
        logger.debug('Starting session...')
        try:            
            global STOP_THREADS
            while not STOP_THREADS:
                #recive info
                rawMsg = s.recv(BUFFER_SIZE)
                #we may have received more than one msg, we have to separate them
                msgs = protocol.separate(rawMsg)
                for msg in msgs:
                    username, data = msg
                    logger.debug('Updating {u}\'s status to {s}'.format(u=username,s=data))
                    _updateData(username,data)
                    if _hasReachedLimit(username):
                        msg = _createProtocolMessage(username,protocol.LIMIT_REACHED)
                        s.send(msg)
        except:
            logger.error('A fatal error ocurred in a thread.')
        finally:
            s.close()
            logger.debug('Connection closed')
    

def _createProtocolMessage(username,status):
    #creates message
    msg = protocol.S2Cmsg(username,status)
    return msg

def _login(s):
    #TODO
    #login, return True if successful
    #https://www.paladion.net/blogs/sending-salted-hashes-just-got#:~:text=Let%27s%20call%20the%20user-specific,is%20Hash(password%2C%20user_salt)
    return True
    
def _updateData(username,data):
    #TODO
    #Updates database data regarding a user.
    pass

def _hasReachedLimit():
    #TODO
    #Retrieves database user usage information and determines whether the user has reached its limit or not
    status = False
    
    #cosas por aquí
    return status

if __name__ == '__main__':
    #runDatabase()
    run()
    
    
    