# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 21:37:00 2019

@author: ecupl
"""

import numpy as np
import pandas as pd
import os
import socket
os.chdir(r"D:\mywork\test")

'''套接字：
AF_UNIX:基于文件
AF_INET:基于网络
面向连接:SOCK_STREAM
无连接:SOCK_DGRAM
'''

#创建套接字(面向连接TCP/IP)
tcpSock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
#无连接UDP/IP
udpSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#####若使用，可简化
from socket import *
tcpSock = socket(AF_INET, SOCK_STREAM)
udpSock = socket(AF_INET, SOCK_DGRAM)


