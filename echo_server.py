# -*- coding: utf-8 -*-
"""
Created on Fri May 26 00:01:21 2023

@author: linft
"""
import logging
import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

logging.basicConfig(format='%(asctime)s: %(message)s', level=logging.INFO,
                    datefmt='%H:%M:%S', force=True)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    logging.info('server:: starting...')
    sock.bind((HOST, PORT))
    sock.listen()
    conn, addr = sock.accept()
    with conn:
        logging.info(f'server:: connected by {addr}')
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
