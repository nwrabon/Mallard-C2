import threading

global hosts
global sockets

global num_hosts
num_hosts = 0

lock = threading.Lock()
