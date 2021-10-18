#! /usr/bin/python3

import socket

server = socket.socket()
ip_port = ('172.16.157.135', 9999)
server.bind(ip_port)
server.listen()
server.accept()
s1, ip = server.accept()

while True:
    data = s1.recv(1024)
    print(data.decode())
    s1.send('ack.{}'.format(data.decode()).encode())

s1.close()

server.close()







