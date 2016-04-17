from genes.debian.traits import is_debian
from genes.mac.traits import is_osx
from genes.ubuntu.traits import is_ubuntu


def get_os():
    if is_debian():
        return 'debian'
    elif is_ubuntu():
        return 'ubuntu'
    elif is_osx():
        return 'osx'
    else:
        raise ValueError('Unknown operating system')
