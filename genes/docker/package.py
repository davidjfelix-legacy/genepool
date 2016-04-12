from genes.apt.get import APTGet
from genes.apt.key import APTKey
from genes.apt.repo import APTRepo
from genes.brew.cask import BrewCask
from genes.debian.traits import is_debian
from genes.linux.traits import get_distro
from genes.linux.traits import get_version
from genes.mac.traits import is_osx
from genes.package import Package
from genes.ubuntu.traits import is_ubuntu


class DockerPkg(Package):
    supported_os_funcs = (
        is_debian,
        is_ubuntu,
    )

    def __init__(self, apt_get=None):
        if apt_get:
            self.apt_get = apt_get
        else:
            self.apt_get = APTGet()
            self.apt_get.update()

    @staticmethod
    def add_deb_repository():
        repository_names = {
            ('ubuntu', '16.04'): 'ubuntu-xenial',
            ('ubuntu', '15.10'): 'ubuntu-wily',
            # Dropped Ubuntu 15.04 Vivid Vervet
            # Dropped Ubuntu 14.10 Utopic Unicorn
            ('ubuntu', '14.04'): 'ubuntu-trusty',
            ('debian', 'sid'): 'debian-stretch',
            ('debian', 'testing'): 'debian-stretch',
            ('debian', '9'): 'debian-stretch',
            ('debian', '8'): 'debian-jessie',
            # Dropped Debian 7 Wheezy
        }

        repo = repository_names.get((get_distro(), get_version()), None)
        if repo is None:
            # FIXME: warn/error
            repo = repository_names.get(('debian', 'sid'))

        apt_key = APTKey()
        apt_repo = APTRepo()

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
            apt_get = APTGet()
            apt_get.update()
            apt_get.install('docker-engine')
        elif is_osx():
            brew_cask = BrewCask()
            brew_cask.update()
            brew_cask.install('dockertoolbox')
        # elif is_alpine():
        #     apk = APK()
        #     apk.add('docker')
        # elif is_arch():
        #     pacman = Pacman()
        #     pacman.sync('docker')
        # elif is_centos() or is_rhel():
        #     self.add_rpm_repository()
        #     yum = YUM()
        #     yum.update()
        #     yum.install('docker-engine')
        # elif is_fedora():
        #     self.add_rpm_repository()
        #     dnf = DNF()
        #     dnf.update()
        #     dnf.install('docker-engine')
        else:
            # FIXME: send error
            pass

    @staticmethod
    def uninstall(*args, **kwargs):
        if is_debian() or is_ubuntu():
            apt = APTGet()
            apt.remove('docker-engine')
        elif is_osx():
            brew_cask = BrewCask()
            brew_cask.uninstall('dockertoolbox')
        # elif is_alpine():
        #     apk = APK()
        #     apk.delete('docker')
        # elif is_arch():
        #     pacman = Pacman()
        #     pacman.remove('docker')
        # elif is_centos() or is_rhel():
        #     yum = YUM()
        #     yum.remove('docker-engine')
        # elif is_fedora():
        #     dnf = DNF()
        #     dnf.remove('docker-engine')
        else:
            # FIXME: Send error
            pass
