# this is the dumb, blocking version
from genes import app, debconf, ppa, brew, cask
import platform

op_sys = platform.system()
dist = platform.linux_distribution()

if os_sys == "Linux" and (dist == 'Ubuntu' or dist == 'Debian'):
    apt.update()
    apt.install('software-properties-common', 'python-software-properties')
    ppa.add('webupd8team/java')
    apt.update()
    debconf.set_selections('oracle-java8-installer', 'shared/accepted-oracle-license-v1-1', 'select', 'true')
    apt.install('oracle-java8-installer')

if os_sys == "Darwin":
    brew.update()
    cask.install('java')
    
if os_sys == "Windows":
    pass #TODO
