#! /usr/bin/python3


"""
### Problems Statement ###
Chat server talks with chat_client
Service Start: bind Ip and port, listening
Connection: being able to connect with multiple clients
Acceptation: receive packets from multiple clients
Service Stop: close socket
Chat Server: Should be a class

"""

import socket
import threading

class chatServer():
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.sock = socket.socket()
    def start(self):
        self.sock.bind((self.ip, self.port))
        self.sock.listen()
        threading.Thread(target=self.accept).start()
    def accept(self):
        while True:
            rsock, raddr = self.sock.accept()
            threading.Thread(target=self.receive, args=(rsock,raddr)).start()

    def receive(self, rsock, raddr):
        while True:
            data_recv = rsock.recv(1024)
            print(data_recv.decode())
            data_send = 'hello\n'
            rsock.send(data_send.encode())

    def stop(self):
        self.sock.close()

server = chatServer('127.0.0.1', 6669)
server.start()


