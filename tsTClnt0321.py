# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 10:24:29 2019

@author: ecupl
"""

from socket import *
from time import ctime

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)       #创建客户端套接字
tcpCliSock.connect(ADDR)       #连接服务器

while True:
    data = input('>')
    if not data:
        break
    tcpCliSock.send(bytes(data,'utf-8'))
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data.decode('utf-8'))
tcpCliSock.close()





