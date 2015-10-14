from genes import apt
import platform

class Config:
    OS = platform.system()
    (DIST, _, CODE) = platform.linux_distribution()
    REPO = DIST.lower() + '-' + CODE

def main():
    if Config.OS == 'Linux':
        if Config.DIST == 'Ubuntu' or Config.DIST == 'Debian':
            apt.recv_keys('58118E89F3A912897C070ADBF76221572C52609D')
            apt.add_repo('docker.list', 'https://apt.dockerproject.org/repo', Config.REPO, 'main')
            apt.update()
            apt.install('docker-engine')
            #FIXME: add compose, machine, etc
        else:
            #FIXME: print failure case
            pass
    elif Config.OS == 'Darwin':
        #brew_cask.install('dockertoolbox')
        pass
    else:
        #FIXME: print failure, handle osx/windows
        pass
