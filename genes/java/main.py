from genes import apt, brew, debconf
from genes.debian import is_debian
from genes.ubuntu import is_ubuntu
from genes.mac import is_osx


def main():
    if is_debian() or is_ubuntu():
        # FIXME: debian needs ppa software
        apt.add_ppa('ppa:webupd8team/java')
        apt.update()
        debconf.set_selections('oracle-java8-installer',
                               'shared/accepted-oracle-license-v1-1',
                               'select', 'true')
        apt.install('oracle-java8-installer')
    elif is_osx():
        brew.update()
        brew.cask_install('java')
    else:
        # FIXME: print failure, handle windows
        pass
