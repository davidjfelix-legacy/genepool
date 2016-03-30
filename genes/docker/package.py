from invoke import task, Collection

from ..apt.get import APTGet
from ..package import Package


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
    def apt_install(self):
        pass

    @task
    def configure(self):
        pass

    @task
    def install(self):
        if is_debian() or is_ubuntu():
            apt = APTGet()
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

    @task
    def uninstall(self):
        pass
