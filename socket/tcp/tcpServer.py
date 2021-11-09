#! /usr/bin/python3

import socket
import threading

# Listening socket
ip_port = ('0.0.0.0', 6666)

# Create a server and start listening
server = socket.socket()
server.bind(ip_port)
server.listen()

# Method receiving and sending data
def com():
    while True:
      s, remote = server.accept()
      print(f'[*] Connecting with {remote}')
      data = s.recv(1024)
      print(data.decode())
      s.send('ack: {}'.format(data.decode()).encode())

# Start receiving and sending data
com_thread = threading.Thread(target = com)
com_thread.start()







