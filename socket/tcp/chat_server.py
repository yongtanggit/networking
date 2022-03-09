#! /usr/bin/python3


"""
### Problems Statement ###
Chat_server talks with chat_client
Service start: bind Ip and port, listening
Connection: being able to connect with multiple clients
Acceptation: receive packets from multiple clients
Re-send: distribute the received packets to all connected clients.
Service stop: close socket
logging: log info on connected clients.
Chat_server: Should be a class

"""

import socket
import threading
import logging

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
            logging.info(raddr)
            logging.info(rsock)
            threading.Thread(target=self.receive, args=(rsock,raddr)).start()

    def receive(self, rsock, raddr):
        while True:
            data = rsock.recv(1024)
            logging.info(data)
            print(data)
            data = 'hello\n'
            rsock.send(data.encode())

    def stop(self):
        self.sock.close()


server = chatServer('127.0.0.1', 6666)
server.start()

