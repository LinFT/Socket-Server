# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 23:28:44 2023

@author: linft
"""
from socket_handler import SocketHandler

data = 'sssssssssssssssssssss'

client_hdlr = SocketHandler()
print(client_hdlr)

client_hdlr.connect()
client_hdlr.send(data)

client_hdlr.recv()
