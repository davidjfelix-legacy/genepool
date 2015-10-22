from genes import apt, brew
from genes import debian
from genes.debian import is_debian
from genes.ubuntu import is_ubuntu
from genes.mac import is_osx


def main():
    if is_debian() or is_ubuntu():
        apt.update()
        apt.install('curl')
        # FIXME: add compose, machine, etc
    elif is_osx():
        brew.cask_install('curl')
    else:
        pass
