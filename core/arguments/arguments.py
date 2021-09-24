from ..graphics.graphics import graphics

import argparse

graphics = graphics()

class arguments:

    mainparse = argparse.ArgumentParser(description=graphics.shell+'\n'+graphics.name+'\n'+graphics.description
                                        ,formatter_class=argparse.RawTextHelpFormatter)
    mainparse.add_argument('payload',help='Your Desired MSF Payload',type=str)
    mainparse.add_argument('interface',help='Your Preferred Network Interface')

    programArgs = mainparse.add_argument_group('Program Switch','Whatcha Gonna Do?')
    programArgs.add_argument('-f','--full',help='Generate Payload & Listener Else Only Generate Listener',action='store_true')

    payloadArgs = mainparse.add_argument_group('Payload','Set Your MSF Payload Options')
    payloadArgs.add_argument('-e','--extension',metavar='',help='Your Desired File Formatting', type=str)
    payloadArgs.add_argument('-o','--output',metavar='',help='Your Desired File Path & Payload Name', type=str)

    networkArgs = mainparse.add_argument_group('Networking','Choose Your Networking Options')
    networkArgs.add_argument('-public',help='Use Public IP Instead Of Local For Payload',action='store_true')

    args = mainparse.parse_args()
