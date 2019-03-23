# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 19:30:17 2019

@author: ecupl
"""

from socket import *

HOST = 'localhost'
PORT = 5677
BUFSIZ = 1024
ADDR = (HOST, PORT)

while True:
    #每次发送消息都会重新连接服务器
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    
    data = input('>')
    if not data:
        break
    tcpCliSock.send(bytes('%s\r\n'%data,'utf-8'))
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data.strip().decode('utf-8'))
    tcpCliSock.close()









