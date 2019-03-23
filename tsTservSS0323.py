# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 19:07:44 2019

@author: ecupl
"""

from socketserver import TCPServer as TCP, StreamRequestHandler as SRH
from time import ctime

HOST=''
PORT=5677
ADDR=(HOST, PORT)

class MyRequestHandler(SRH):
    #重写handle()方法
    def handle(self):
        print('connect from:',self.client_address)
        self.wfile.write(bytes('[%s] %s'%(ctime(),self.rfile.readline()),'utf-8'))

tcpServ = TCP(ADDR, MyRequestHandler)
print('waiting for connection...')
tcpServ.serve_forever()
    





