'''
### Problems Statement ###
Chat_server talks with chat_client
Service start: bind Ip and port, listening
Connection: being able to connect with multiple clients
Acceptation: receive packets from multiple clients
Re-send: distribute the received packets to all connected clients.
Service stop: close socket
logging: log info on connected clients.
Chat_server: Should be a class

'''

import socket
from threading import Thread

class chatServer():
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.sock = socket.socket()
    def start(self):
        self.sock.bind((self.ip, self.port))
        self.sock.listen()
        while True:
            connection = Thread(target=self.accept)
            connection.start()
    def accept(self):
        rsock, raddr = self.sock.accept()
        while True:
            data = rsock.recv(1024)
            print(data)
            data = 'hello\n'
            rsock.send(data.encode())

    def stop(self):
        self.sock.close()


server = chatServer('127.0.0.1', 6666)
server.start()
# server.stop()

