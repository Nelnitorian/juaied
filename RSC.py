# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""

    Glosario:
        -RSC: Radius server que se porta como cliente al enviar la base de datos al BS
        -BS: Billing server que se porta como servidor al recibir la base de datos enviada por el RSC


"""

import socket

TCP_IP = 'localhost'
TCP_PORT = 9001
BUFFER_SIZE = 1024
INTERVAL = 10 #seconds

def run():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    if login(s):
        with openDbFile() as f:
            print ('file opened')
            while True:
                #print('receiving data...')
                data = s.recv(BUFFER_SIZE)
                print('data=%s', (data))
                if not data:
                    f.close()
                    print ('file close()')
                    break
                # write data to a file
                f.write(data)
        
        print('Successfully get the file')
        s.close()
        print('connection closed')

def login(s):
    return True

def openDbFile():
    f = open('received_file', 'wb')
    return f

if __name__ == '__main__':
    run()