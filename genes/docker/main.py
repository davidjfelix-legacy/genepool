from genes.apt import commands as apt
from genes.brew import commands as brew
from genes import debian
from genes.debian.traits import is_debian
from genes.ubuntu.traits import is_ubuntu
from genes.mac.traits import is_osx


def main():
    if is_debian() or is_ubuntu():
        repo = debian.traits.distribution.lower() + '-' + \
               debian.traits.codename.lower()
        apt.recv_keys('58118E89F3A912897C070ADBF76221572C52609D')
        apt.add_repo('deb', 'https://apt.dockerproject.org/repo', repo, 'main')
        apt.update()
        apt.install('docker-engine')
        # FIXME: add compose, machine, etc
    elif is_osx():
        brew.cask_install('dockertoolbox')
    else:
        # FIXME: print failure, handle osx/windows
        pass
