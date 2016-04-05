from genes.apt.get import APTGet
from genes.debian.traits import is_debian
from genes.mac.traits import is_osx
from genes.systemsetup import commands as systemsetup
from genes.ubuntu.traits import is_ubuntu


def main():
    if is_debian() or is_ubuntu():
        apt_get = APTGet()
        apt_get.update()
        apt_get.install('openssh-server')
    elif is_osx():
        systemsetup.systemsetup('-setremotelogin', 'on')
    else:
        pass
