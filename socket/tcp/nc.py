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
import threading
import subprocess
'''
parser = argparse.ArgumentParser()
parser.add_argument('-t', nargs='?',type=str,help='host')
parser.add_argument('-p', nargs='?', type=int, help='port')
parser.add_argument('-e', nargs='?',type=str, help='excute command')
parser.add_argument('-u', nargs='?',type=str, help='upload to file')
parser.add_argument('-l', action='store_true', help='listen')
parser.add_argument('-c', action='store_true', help='command shell')
opt=parser.parse_args()

## client mode

def client():
    message = input('connected: say something: ')
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip,port))
    cleint.send(b"message")
    response = cleint.recv(1024)
    print(response.decode())
    client.close()


## server mode
ip ='127.0.0.1'
port = 6666


server = socket.socket()
server.bind((ip,port))
server.listen()
print(f'[*] Listening on {(ip,port)}')



def server_stdout():
    while True:
       s,r_ip_port = server.accept()
       print(f'[*] Connecting from: {r_ip_port})')
       data = s.recv(1024)
       print(f'Data received: {data}'.decode())
       s.send(b'back -> {data}')
server_stdout_thread = threading.Thread(target = server_stdout)
server_stdout_thread.start()


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
          break
'''
def server_execute(cmd):
    cmd = cmd.strip()
    if not cmd:
        return
    result= subprocess.check_output(cmd)
    result=(result.decode())
    return result


def server_shell():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 6666))
    while True:
       client.send(b"#> ")
       cmd = client.recv(1024).decode()
       result = server_execute(cmd)
       client.send(result.encode())




server_shell()























