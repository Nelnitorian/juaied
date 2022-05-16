# -*- coding: utf-8 -*-
"""
Created on Mon May 16 09:07:24 2022

@author: jujor
"""

import socket,time,src.protocol

TCP_IP = 'localhost'
TCP_PORT = 9001
BUFFER_SIZE = 1024


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((TCP_IP, TCP_PORT))

s.listen(2)


(conn, (ip,port)) = s.accept()

time.sleep(5)
s.close()