from genes.apt import commands as apt
from genes.brew import commands as brew
from genes.debian.traits import is_debian
from genes.mac.traits import is_osx
from genes.ubuntu.traits import is_ubuntu


def main():
    if is_debian() or is_ubuntu():
        apt.update()
        apt.install('asciinema')
    elif is_osx():
        brew.update()
        brew.install('asciinema')
    else:
        # FIXME: print failure, handle windows
        pass
