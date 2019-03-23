# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 10:24:29 2019

@author: ecupl
"""

from socket import *
from time import ctime
import os

HOST = ''
PORT = 21567
BUFSIZ = 10240
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)       #创建服务器套接字
tcpSerSock.bind(ADDR)       #绑定地址（主机名+端口）
tcpSerSock.listen(5)        #开启TCP监听器，并设置传入连接请求最大数

while True:
    #等待客户端连接
    print('waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('connection from :',addr)
#    print('tcpCliSock: %s'%tcpCliSock)
    #客户端交互
    while True:
       data = tcpCliSock.recv(BUFSIZ)
       data = data.decode('utf-8')
       responsedic = {'date':ctime(), 'os':os.name, 'ls':str(os.listdir(os.curdir))}
       if not data:
           break
       elif responsedic.get(data):
           tcpCliSock.send(bytes(responsedic[data],'utf-8'))
       else:
           tcpCliSock.send((bytes('[%s] %s'%(ctime(),data),'utf-8')))
    tcpCliSock.close()      #关闭客户端对话
tcpSerSock.close()      #关闭服务器






