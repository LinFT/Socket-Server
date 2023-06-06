# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 00:25:28 2023

@author: linft
"""

import socket

HOST = '127.0.0.1'
PORT = 65432

class SocketHandler:
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock
    
    def connect(self, host=HOST, port=PORT):
        self.host = host
        self.port = port
        self.sock.connect((host, port))
        print(f'Socket:: connecting to {HOST} on {PORT}')
    
    def send(self, data):
        try:
            data = str.encode(data)
        except:
            pass
        
        totalsent = 0
        while totalsent < len(data):
            sent = self.sock.send(data[totalsent:])
            if sent == 0:
                raise RuntimeError('socket connection broken')
            totalsent += sent
    
    def recv(self, EOF='\036'):
        chunks = []
        bytes_recved = 0
        #self.sock.setblocking(False)
        while True:
            chunk = self.sock.recv(1024)
            print(f'Socket:: received {chunk}')
            if chunk == b'':
                raise RuntimeError('socket connection broken')
            chunks.append(chunk)
            bytes_recved += len(chunk)
        
        data = b''.join(chunks).decode()
        return data
    