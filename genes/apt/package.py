from genes.dpkg.commands import Dpkg
from genes.package import Package


class APTPkg(Package):
    @staticmethod
    def uninstall(*args, **kwargs):
        pass

    @staticmethod
    def configure(*args, **kwargs):
        pass

    @staticmethod
    def is_installed(*args, **kwargs):
        if len(args) == 0:
            raise ValueError('missing package argument')
        else:
            return Dpkg.is_package_installed(args[0])

    @staticmethod
    def install(*args, **kwargs):
        pass
