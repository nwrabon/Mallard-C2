from rich.table import Table
import pickle
import codecs

possible_commands = {
    "" : "",
    "" : "",
    "" : "",
    "" : "",
    "" : "",
    "" : "",
    "" : "",
    "" : "",
    "" : ""
}

# handle hosts command (show all hosts)
# @pre
#   conn is socket connected where table will be sent
#   hosts is a list of tuples in form [(id, ip, status)] 
# TODO if host is inactive show data in red if active green
def send_hosts_table(conn, hosts):
    table = Table(title="Hosts", show_lines=True)
    table.add_column("IP", justify='right')
    table.add_column("Port", justify="left")
    table.add_column("Status", justify='right')

    for i in hosts:

        table.add_row(i[0][0], str(i[0][1]), i[2])

        # encodes obj to bytes to send over network
    pickled = codecs.encode(pickle.dumps(table), "base64")
    conn.send(pickled)