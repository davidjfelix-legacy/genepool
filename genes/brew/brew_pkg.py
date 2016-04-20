import shutil

from genes.curl.commands import Curl
from genes.os.traits import get_os
from genes.package import Package
from genes.ruby.commands import Ruby


class BrewPkg(Package):
    def __init__(self, os_name=None):
        self.os_name = os_name if os_name else get_os()

    @staticmethod
    def is_installed():
        return shutil.which("brew") is not None

    @staticmethod
    def uninstall():
        if BrewPkg.is_installed():
            Curl.download(
                    'https://raw.githubusercontent.com/Homebrew/install/master/uninstall',
                    '/tmp/brew_uninstall'
            )
            ruby = Ruby()
            ruby.run('-e', '/tmp/brew_uninstall')

    @staticmethod
    def configure(*args, **kwargs):
        pass

    @staticmethod
    def install():
        if not BrewPkg.is_installed():
            Curl.download(
                    'https://raw.githubusercontent.com/Homebrew/install/master/install',
                    '/tmp/brew_install'
            )
            ruby = Ruby()
            ruby.run('-e', '/tmp/brew_install')
