from genes.apt import get as apt
from genes.brew import commands as brew
from genes.debian.traits import is_debian
from genes.ubuntu.traits import is_ubuntu
from genes.mac.traits import is_osx


def main():
    if is_debian() or is_ubuntu():
        apt.update()
        apt.install('curl')
    elif is_osx():
        brew.install('curl')
    else:
        pass
