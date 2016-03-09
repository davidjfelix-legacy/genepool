from genes import directory
from genes.alpine.traits import is_alpine
from genes.apk import commands as apk
from genes.apt import commands as apt
from genes.arch.traits import is_arch
from genes.brew import commands as brew
from genes.centos.traits import is_centos
from genes.curl.commands import download
from genes.debian.traits import is_debian, get_codename
from genes.directory import DirectoryConfig
from genes.dnf import commands as dnf
from genes.fedora.traits import is_fedora
from genes.gentoo.traits import is_gentoo
from genes.gnu_coreutils.commands import chmod, ln
from genes.lib.traits import if_any_funcs
from genes.linux.traits import get_distro
from genes.mac.traits import is_osx
from genes.pacman import commands as pacman
from genes.redhat.traits import is_rhel
from genes.ubuntu.traits import is_ubuntu
from genes.windows.traits import is_windows
from genes.yum import commands as yum

supported_os_funcs = (
    is_alpine,
    is_arch,
    is_centos,
    is_debian,
    is_fedora,
    is_gentoo,
    is_osx,
    is_rhel,
    is_ubuntu,
    is_windows,
)


@if_any_funcs(is_ubuntu, is_debian)
def install_compose():
    compose_version = "1.5.2"
    compose_url = "https://github.com/docker/compose/releases/download/" + \
                  compose_version + "/docker-compose-Linux-x86_64"
    compose_directory = "/opt/docker-compose"
    compose_executable = compose_directory + "/docker-compose-" + compose_version

    def config_directory():
        return DirectoryConfig(
                path=compose_directory,
                mode='755',
                group='root',
                user='root',
        )

    # FIXME: Need to find a way to handle errors here
    directory.main(config_directory)
    download(compose_url, compose_executable)
    chmod('755', compose_executable)
    # FIXME: handle file exists
    ln("-s", compose_executable, "/usr/local/bin/docker-compose")


@if_any_funcs(is_ubuntu, is_debian)
def install_machine():
    machine_version = '0.6.0'
    machine_url = 'https://github.com/docker/machine/releases/download/v' + \
                  machine_version + '/docker-machine-Linux-x86_64'
    machine_directory = '/opt/docker-machine'
    machine_executable = machine_directory + '/docker-machine-' + machine_version

    def config_directory():
        return DirectoryConfig(
                path=machine_directory,
                mode='755',
                group='root',
                user='root',
        )

    directory.main(config_directory)
    download(machine_url, machine_executable)
    chmod('755', machine_executable)
    ln('-s', machine_executable, '/usr/local/bin/docker-machine')


def add_yum_repo():
    pass


@if_any_funcs(*supported_os_funcs)
def install():
    if is_debian() or is_ubuntu():
        repo = get_distro().lower() + '-' + \
               get_codename().lower()
        apt.recv_keys('58118E89F3A912897C070ADBF76221572C52609D')
        apt.add_repo('deb', 'https://apt.dockerproject.org/repo', repo, 'main')
        apt.update()
        apt.install('docker-engine')
    elif is_osx():
        brew.update()
        brew.cask_install('dockertoolbox')
    elif is_alpine():
        apk.add('docker')
    elif is_arch():
        pacman.sync('docker')
    elif is_centos() or is_rhel():
        add_yum_repo()
        yum.update()
        yum.install('docker-engine')
    elif is_fedora():
        add_yum_repo()
        dnf.update()
        dnf.install('docker-engine')
    elif is_gentoo():
        pass
    elif is_windows():
        pass
    else:
        pass


def main():
    install()
