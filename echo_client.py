# -*- coding: utf-8 -*-
"""
Created on Fri May 26 00:24:58 2023

@author: linft
"""
import logging
import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

logging.basicConfig(format='%(asctime)s: %(message)s', level=logging.INFO,
                    datefmt='%H:%M:%S', force=True)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    sock.sendall(b'Hello, world')
    data = sock.recv(1024)

logging.info(f'client:: Received {data!r}')
