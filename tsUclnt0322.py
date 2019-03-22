# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 21:02:53 2019

@author: ecupl
"""

from socket import *

#创建UDP客户端
HOST='localhost'
PORT=5677
BUFSIZ=1024
ADDR=(HOST,PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('>')
    if not data:
        break
    udpCliSock.sendto(bytes(data,'utf-8'),ADDR)
    data, addr = udpCliSock.recvfrom(BUFSIZ)
    if not data:
        break
    print(data.decode('utf-8'))
    print('receive from {}'.format(addr))
udpCliSock.close()




