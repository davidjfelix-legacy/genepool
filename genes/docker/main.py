from genes.apt import commands as apt
from genes.brew import commands as brew
from genes.curl.commands import download
from genes.debian.traits import is_debian, get_codename
from genes.lib.traits import if_any_funcs
from genes.linux.traits import get_distro
from genes.mac.traits import is_osx
from genes.ubuntu.traits import is_ubuntu


@if_any_funcs(is_ubuntu, is_debian)
def install_compose():
    compose_version = "1.5.2"
    def config_directory():
        return DirectoryConfig(
            path='/opt/docker-compose',
            mode='755',
            group='root',
            user='root',
        )

    # FIXME: Need to find a way to handle errors here
    directory.main(config_directory)
    download(
        "https://github.com/docker/compose/releases/download/" + compose_version + "/docker-compose-Linux-x86_64",
        "/opt/docker-compose/docker-compose
    )
    


@if_any_funcs(is_ubuntu, is_debian)
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
        install_compose()
        install_machine()
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
