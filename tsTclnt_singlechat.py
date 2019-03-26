# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 23:10:28 2019

@author: ecupl
"""

from socket import *

HOST = 'localhost'
PORT = 5677
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('>')
    if not data:
        continue
    elif data=='quit':
        tcpCliSock.send(bytes(data,'utf-8'))
        break
    tcpCliSock.send(bytes(data,'utf-8'))
    data = tcpCliSock.recv(BUFSIZ)
    print(data.decode('utf-8'))
tcpCliSock.close()







