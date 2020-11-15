#!/usr/bin/python3

## This program has two functions:
## 1) Send message 2) Receive message
## I wrote this program to understant how udp socket works with Python. 
## Two options control the behaviours of this program:
## 1) -s (sending) 2) -r (receiving message)
## I also leaned how to use "argparse model".  

import argparse
import socket

# process options
def option():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s',help='Send message',action='store_true')
    parser.add_argument('-r',help='Receive message',action='store_true')
    parser.add_argument('--ip',help='IP address')
    parser.add_argument('--port',help='Port',type=int)
    args=parser.parse_args()
    return args

# send message
def sender(ip,port):
    message=input('Message(EXIT to exit): ')
    if message == 'EXIT':
        sys.exit()
    else:
        udp_socket.sendto(message.encode(),(ip, port))
        udp_socket.close

# Message receiver
def receiver(port):
    udp_socket.bind(port)
    while True:
         data=udp_socket.recvfrom(4096)
         message=data[0]
         print(message.decode())
         udp_socket.close


# Create a Socket
udp_socket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Main
args=option()

if args.s:
    ip=args.ip
    port=args.port
    while True:
          sender(ip,port)

if args.r:
    port=args.port
    port=('',port)
    receiver(port)



        

    





    











