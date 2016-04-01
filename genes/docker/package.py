from invoke import task, Collection

from genes.apt.get import APTGet
from genes.apt.key import AptKey
from genes.apt.repo import AptRepo
from genes.debian.traits import is_debian
from genes.linux.traits import get_codename
from genes.linux.traits import get_distro
from genes.package import Package
from genes.ubuntu.traits import is_ubuntu


class DockerPkg(Package):
    supported_os_funcs = (
        is_debian,
        is_ubuntu,
    )

    def __init__(self):
        self.collection = Collection('docker')
        self.collection.add_task(self.configure)
        self.collection.add_task(self.install)
        self.collection.add_task(self.uninstall)

    @task
    def add_deb_repository(self):
        repo = get_distro().lower() + '-' + \
               get_codename().lower()

        apt_key = AptKey()
        apt_repo = AptRepo()

        apt_key.recv_keys('58118E89F3A912897C070ADBF76221572C52609D')
        apt_repo.add_repo('deb https://apt.dockerproject.org/repo ' + repo + ' main')


    @task
    def add_rpm_repository(self):
        pass

    @task
    def configure(self):
        pass

    @task
    def install(self):
        if is_debian() or is_ubuntu():
            self.add_deb_repository()
            apt = APTGet()
            apt.update()
            apt.install('docker-engine')
        else:
            pass
        """elif is_osx():
            brew = Brew()
            brew.update()
            brew.cask_install('dockertoolbox')
        elif is_alpine():
            apk = APK()
            apk.add('docker')
        elif is_arch():
            pacman = Pacman()
            pacman.sync('docker')
        elif is_centos() or is_rhel():
            self.add_rpm_repository()
            yum = YUM()
            yum.update()
            yum.install('docker-engine')
        elif is_fedora():
            self.add_rpm_repository()
            dnf = DNF()
            dnf.update()
            dnf.install('docker-engine')"""

    @task
    def uninstall(self):
        if is_debian() or is_ubuntu():
            apt = APTGet()
            apt.remove('docker-engine')
        else:
            pass
        """elif is_osx():
            brew = Brew()
            brew.cask_uninstall('dockertoolbox')
        elif is_alpine():
            apk = APK()
            apk.delete('docker')
        elif is_arch():
            pacman = Pacman()
            pacman.remove('docker')
        elif is_centos() or is_rhel():
            yum = YUM()
            yum.remove('docker-engine')
        elif is_fedora():
            dnf = DNF()
            dnf.remove('docker-engine')"""
