# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 22:59:08 2019

@author: ecupl
"""

from socket import *

HOST = ''
PORT = 5677
BUFSIZ = 1024
ADDR = (HOST, PORT)

#创建TCP套接字
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

#接受服务端消息并处理
while True:
    print('waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('connect from %s',addr)
    while True:
        data = tcpCliSock.recv(BUFSIZ)
        data = data.decode('utf-8')
        if data == 'quit':
            print('即将退出')
            break
        else:
            print('%s said %s'%(addr,data))
        senddata = ''
        if senddata == '':
            senddata = input('>')
        tcpCliSock.send(bytes(senddata,'utf-8'))
    tcpCliSock.close()
#        data = None
tcpSerSock.close()









