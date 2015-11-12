from genes.apt import commands as apt
from genes.brew import commands as brew
from genes.ubuntu.traits import is_ubuntu
from genes.debian.traits import is_debian
from genes.mac.traits import is_osx


def main():
    if is_ubuntu() or is_debian():
        apt.update()
        apt.install('golang')
    elif is_osx():
        brew.update()
        brew.install('go')
    else:
        pass
