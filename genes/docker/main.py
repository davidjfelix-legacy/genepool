from genes import apt, brew
from genes import debian
from genes.debian import is_debian
from genes.ubuntu import is_ubuntu
from genes.mac import is_osx


def main():
    if is_debian() or is_ubuntu():
        repo = debian.traits.distribution.lower() + '-' + \
               debian.traits.codename.lower()
        apt.recv_keys('58118E89F3A912897C070ADBF76221572C52609D')
        apt.add_repo('https://apt.dockerproject.org/repo', repo, 'main')
        apt.update()
        apt.install('docker-engine')
        # FIXME: add compose, machine, etc
    elif is_osx():
        brew.cask_install('dockertoolbox')
    else:
        # FIXME: print failure, handle osx/windows
        pass
