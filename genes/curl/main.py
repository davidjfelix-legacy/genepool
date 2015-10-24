from genes import apt, brew
from genes.debian import is_debian
from genes.ubuntu import is_ubuntu
from genes.mac import is_osx


def main():
    if is_debian() or is_ubuntu():
        apt.update()
        apt.install('curl')
    elif is_osx():
        brew.install('curl')
    else:
        pass
