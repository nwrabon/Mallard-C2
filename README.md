# Mallard-C2
Originally made to teach the public about c2 servers and how attackers can use them for malicious purposes.  Created to have very visual effects so less tech-savy viewers can easily understand the dangers. 

Demoed at Clemson University Watt Center.

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

6. With the victim now connected to the server you can browse to the website located at http://<server_ip>:5000 on an attacker machine. 
    There will be a list of victims connected and you can run different prankish payloads on the victim.

