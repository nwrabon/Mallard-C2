from rich import print as rprint
from rich.prompt import Prompt as prompt
import clipboard
import socket


# Client Side 

# TODO: conn keepalive
# sock.ioctl(socket.SIO_KEEPALIVE_VALS, (1, 60000, 30000))

# Create Client session; listen to server
server_addr = ('localhost', 13337)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.connect(server_addr)
    rprint("Connected")
except:
    rprint("Connection Failed")
    exit(0)

while True:
    # Prompt user for input
    msg = prompt.ask('[bold dark_orange]>>')
    if msg == 'quit':
        sock.close()
        exit(0)
    elif len(msg) != 0:
        sock.send(msg.encode())
        data = sock.recv(1024).decode()
        rprint("Received_data: [green1]%s" % data)
        # TODO: handle commands coming back

    # if data.decode() == "clipboard":
    # text = clipboard.paste()
    # sock.send(text.encode())

