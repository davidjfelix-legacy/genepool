from genes import apt
import platform

class Config:
    OS = platform.system()
    DIST = platform.linux_distribution()

def main():
    if Config.OS == 'Linux':
        if Config.DIST[0] == 'Ubuntu' or Config.DIST[0] == 'Debian':
            apt.recv_key('58118E89F3A912897C070ADBF76221572C52609D')
