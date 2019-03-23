# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 20:48:09 2019

@author: ecupl
"""

###创建Twisted Reactor TCP服务器
from twisted.internet import protocol,reactor
from time import ctime

PORT = 5677

class TSServProtocol(protocol.Protocol):
    def connectionMade(self):
        Clnt = self.Clnt = self.transport.getPeer().host
        print('...connected from:',Clnt)
    def dataReceived(self,data):
        self.transport.write('[%s] %s'%(ctime(),data))

#创建协议工厂
factory = protocol.Factory()
factory.protocol = TSServProtocol
print('waiting for connection...')
reactor.listenTCP(PORT,factory)
reactor.run()






