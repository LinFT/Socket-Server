# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 21:50:44 2023

@author: linft
"""
import socket
import threading
from pathlib import Path
from socket_handler import HOST, PORT, SocketHandler, ErrorCatcher

filename = Path(__file__).parent / 'tmp.txt'

clients = []

def client_handler(sock):
    sock_hdlr = SocketHandler(sock)
    with ErrorCatcher():
        file_buffer = sock_hdlr.recv()
        print(f'Server:: received {file_buffer}')
    
    try:
        with open(filename, 'wb') as f:
            f.write(file_buffer)
        sock_hdlr.send(f'Server:: successfully saved file to {filename}\n')
    except:
        sock_hdlr.send(f'Server:: failed to save file to {filename}\n')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.setblocking(False)
    
    print(f'Server:: listening to {HOST} on {PORT}')
    server.listen(5)
    
    while True:
        with ErrorCatcher():
            client, addr = server.accept()
            print(f'Server:: connected by {addr}')
            
            client.setblocking(False)
            clients.append(client)
            
            client_td = threading.Thread(target=client_handler, args=(client,))
            client_td.start()
