# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""

    Glosario:
        -RSC: Radius server que se porta como cliente al enviar la base de datos al BS
        -BS: Billing server que se porta como servidor al recibir la base de datos enviada por el RSC


"""


import socket
from threading import Thread

TCP_IP = 'localhost'
TCP_PORT = 9001
BUFFER_SIZE = 1024
INTERVAL = 10 #seconds

class ClientThread(Thread):

    def __init__(self,ip,port,sock):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
        print (" New thread started for "+ip+":"+str(port))

    def run(self):
        filename='mytext.txt'
        f = open(filename,'rb')
        while True:
            l = f.read(BUFFER_SIZE)
            while (l):
                self.sock.send(l)
                #print('Sent ',repr(l))
                l = f.read(BUFFER_SIZE)
            if not l:
                f.close()
                self.sock.close()
                break
def run():
    tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcpsock.bind((TCP_IP, TCP_PORT))
    threads = []
    
    while True:
        tcpsock.listen(1)
        print ("Waiting for incoming connections...")
        (conn, (ip,port)) = tcpsock.accept()
        print ('Got connection from ', (ip,port))
        newthread = ClientThread(ip,port,conn)
        newthread.start()
        threads.append(newthread)
    
    for t in threads:
        t.join()
    
        
if __name__ == '__main__':
    run()
    
