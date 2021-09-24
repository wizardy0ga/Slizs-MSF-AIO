from ..format.formatting import notifications
from ..format.formatting import coloration
from sys import exit

import netifaces
import requests

colors = coloration()
notify = notifications()

class ipAddress:

    def __init__(self):
        self.portForward = '4444' #Change this to select your port

    def getLocalip(self,interf):
        try:
            interface = netifaces.ifaddresses(interf)

        except ValueError:
            exit(f"{notify.warning}{colors.red} Error! Please Use Valid Network Interface. Quitting...")

        else:
            nic = interface[2]
            stripDict = nic[0]
            localIP = stripDict.get('addr')
            return localIP

    def getPublicIPstring(self):

        self.myPublicIP = requests.get('https://api.ipify.org').text
        return self.myPublicIP