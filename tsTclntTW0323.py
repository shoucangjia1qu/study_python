# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 21:02:59 2019

@author: ecupl
"""

from twisted.internet import protocol, reactor

HOST = 'localhost'
PORT = 5677

class TSClntProtocol(protocol.Protocol):
    def sendData(self):
        data = input('>')
        if data:
            print('...sending %s'%data)
            self.transport.write(data)
        else:
            self.transport.loseConnection()
    
    def connectionMade(self):
        self.sendData()
    
    def dataReceived(self,data):
        print(data)
        self.sendData()

class TSClntFactory(protocol.ClientFactory):
    protocol = TSClntProtocol
    clientConnectionLost = clientConnectionFailed = lambda self,connector,reason: reactor.stop()
    
reactor.connectTCP(HOST, PORT, TSClntFactory())
reactor.run()




