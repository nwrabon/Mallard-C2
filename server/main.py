from rich import print as rprint
import common
import controllers.views
import datetime
import flask
import threading
import socket


sockets = []


def handle_connection(conn, ip):
    sockets.append(conn)

    # TODO fix access of global var from separate threads
    with common.lock:
        common.hosts.append((ip, datetime.datetime.now()))
        print(common.hosts)

    rprint(f"[bold green]Connected by {ip}")

    conn.send(duck.encode())


def listen_for_connections():
    try:
        while True:
            # create a dedicated thread for each incoming connection
            conn, addr = s.accept()
            t = threading.Thread(target=handle_connection, args=(conn, addr))
            t.start()
    except Exception as e:
        rprint("[red]Error: %s" % str(e))
        [sock.close() for sock in sockets]


# run web ui and handle client connections
if __name__ == '__main__':
    # load ascii art
    file = open('../art/duck.ansi', 'r')
    duck = file.read()
    file.close()

    # setup socket
    server_addr = ("localhost", 1337)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(server_addr)
    s.listen(5)

    print('CSOC C2 Server')
    threading.Thread(target=lambda: listen_for_connections()).start()

    flask_app = flask.Flask(__name__)
    flask_app.register_blueprint(controllers.views.view_routes)
    # threading.Thread(target=lambda: flask_app.run(use_reloader=False)).start()
    flask_app.run()

