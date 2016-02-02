from genes.apt import commands as apt
from genes.brew import commands as brew
from genes.debian.traits import is_debian, get_codename
from genes.linux.traits import get_distro
from genes.mac.traits import is_osx
from genes.ubuntu.traits import is_ubuntu


def install_compose():
    pass


def install_machine():
    pass


def main():
    if is_debian() or is_ubuntu():
        repo = get_distro().lower() + '-' + \
               get_codename().lower()
        apt.recv_keys('58118E89F3A912897C070ADBF76221572C52609D')
        apt.add_repo('deb', 'https://apt.dockerproject.org/repo', repo, 'main')
        apt.update()
        apt.install('docker-engine')
        # FIXME: add compose, machine, etc
    elif is_osx():
        brew.update()
        brew.cask_install('dockertoolbox')
    # elif is_alpine()
    # elif is_arch()
    #     pacman.update()
    #     pacman.install('docker')
    #     # start docker service
    #     # add compose, machine
    else:
        # FIXME: print failure, handle osx/windows
        pass
