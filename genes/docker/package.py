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
        pass

    @staticmethod
    def add_deb_repository():
        repo = get_distro().lower() + '-' + \
               get_codename().lower()

        apt_key = AptKey()
        apt_repo = AptRepo()

        apt_key.recv_keys('58118E89F3A912897C070ADBF76221572C52609D')
        apt_repo.add_repo('deb https://apt.dockerproject.org/repo ' + repo + ' main')

    @staticmethod
    def add_rpm_repository():
        pass

    @staticmethod
    def configure(*args, **kwargs):
        pass

    @staticmethod
    def install(*args, **kwargs):
        if is_debian() or is_ubuntu():
            DockerPkg.add_deb_repository()
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

    @staticmethod
    def uninstall(*args, **kwargs):
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
