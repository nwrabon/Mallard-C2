from rich import print as rprint
from datetime import datetime
from aiohttp import web

from commands import *

import aiohttp
import threading
import time
import socket
import sys

# list of hosts
host_dict = {'555.55.555.55' : 'active'}

# Holds post-exploitation commands for the target host that the operator will enter
commands = [] 

# load ascii art
file = open('duck.ansi', 'r')
duck = file.read()
file.close()

#===========SERVER CREATION=============
print('CSOC C2 Server')

HOST = "127.0.0.1"
PORT = 13337
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

def handle_connection(conn, ip):
    rprint(f"[bold green]Connected by {ip}")
    conn.send(duck.encode())
    msg = conn.recv(1024).decode()

    #act as echo server
    while msg != 'quit' and len(msg) != 0: 
        rprint("Received_data: [green]%s" % msg)


        if msg == 'hosts':
            send_hosts_table(conn, host_dict)

        else:
            conn.send(msg.encode())


        msg = conn.recv(1024).decode()
    conn.close()
    rprint("[red]Connection Closed: %s" %str(ip))


# def init_server():
while True:
    # create a dedicated thread for each incoming connection
    conn, addr = s.accept()
    t = threading.Thread(target=handle_connection, args=(conn, addr))
    t.start()


