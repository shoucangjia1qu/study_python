# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 20:31:13 2019

@author: ecupl
"""

from socket import *
from time import ctime
import os

os.chdir(r'D:\mywork\test')
#创建UDP时间戳服务器
HOST=''
PORT=5677
BUFSIZ=1024
ADDR=(HOST,PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print('waiting for message...')
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    data = data.decode('utf-8')
    udpSerSock.sendto(bytes('[%s] %s'%(ctime(),data), 'utf-8'), addr)
    print('...received from and returned to:',addr)
udpSerSock.close()






