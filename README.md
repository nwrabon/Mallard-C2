# CSOC-C2
A simple C2 server to demo at Clemson Watt Center

# Install
pip install -r requirements.txt

# Usage
1. start server - `python3 /server/main.py`
2. modify the ip in CLI.py to that of the server.
3. connect to server via CLI on a windows machine - `python3 /client/CLI.py`
4. generate executable with - `agent <ip of server>`
5. place the executable on the victim machine(windows) and run it

### Note:
You may need to disable real time protection on the victim for all payloads to work correctly. 

6. With the victim now connected to the server you can browse the the website located at http://<server_ip>:5000
    There will be a list of victims connected and you can run different prankish payloads on the victim.

