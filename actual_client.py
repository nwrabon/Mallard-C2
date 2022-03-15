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
    duck = sock.recv(14434).decode()
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
    elif msg != '':
        sock.send(msg.encode())
        msg = sock.recv(1024).decode()
        rprint("Received_msg: [green1]%s" % msg)

    # if msg.decode() == "clipboard":
    # text = clipboard.paste()
    # sock.send(text.encode())

