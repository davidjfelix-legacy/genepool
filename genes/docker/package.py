from genes.brew.command import Brew
from invoke import task, Collection

from genes.apt.get import APTGet
from genes.debian import is_debian
from genes.mac import is_osx
from genes.package import Package


class DockerPkg(Package):
    def __init__(self):
        self.collection = Collection('docker')
        self.collection.add_task(self.configure)
        self.collection.add_task(self.install)
        self.collection.add_task(self.uninstall)

    @task
    def add_deb_repository(self):
        pass

    @task
    def add_rpm_repository(self):
        pass

    @task
    def apt_install(self):
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
        elif is_osx():
            brew = Brew()
            brew.update()
            brew.cask_install('dockertoolbox')
        else:
            pass
        """elif is_alpine():
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
        elif is_osx():
            brew = Brew()
            brew.cask_uninstall('dockertoolbox')
        else:
            pass
        """elif is_alpine():
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
