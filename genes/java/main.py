from genes import apt, debconf
import platform

class Config:
    OS = platform.system()
    (DIST, _, CODE) = platform.linux_distribution()
    REPO = DIST.lower() + '-' + CODE

def main():
    if Config.OS == 'Linux':
        if Config.DIST == 'Ubuntu' or Config.DIST == 'Debian':
            #FIXME: debian needs ppa software
            apt.add_ppa('ppa:webupd8team/java')
            apt.update()
            debconf.set_selections('oracle-java8-installer',
                                   'shared/accepted-oracle-license-v1-1',
                                   'select', 'true')
            apt.install('oracle-java8-installer')
        else:
            #FIXME: print failure case
            pass
    elif Config.OS == 'Darwin':
        #brew_cask.install('java8')
        pass
    else:
        #FIXME: print failure, handle windows
        pass
