import socket


# TODO: conn keepalive
# sock.ioctl(socket.SIO_KEEPALIVE_VALS, (1, 60000, 30000))

server_addr = ('localhost', 1337)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect(server_addr)
    duck = sock.recv(14434).decode()
    print(duck)
except:
    exit(0)

while True:
    msg = sock.recv(1024).decode()

    if msg == 'quit':
        sock.close()
        exit(0)
    elif msg != '':
        sock.send(msg.encode())
