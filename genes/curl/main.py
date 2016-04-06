from genes.apt.get import APTGet
from genes.brew.brew import Brew
from genes.debian.traits import is_debian
from genes.mac.traits import is_osx
from genes.ubuntu.traits import is_ubuntu


def main():
    if is_debian() or is_ubuntu():
        apt_get = APTGet()
        apt_get.update()
        apt_get.install('curl')
    elif is_osx():
        brew = Brew()
        brew.update()
        brew.install('curl')
    else:
        pass
