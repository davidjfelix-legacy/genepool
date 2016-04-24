import subprocess

from genes.brew.brew_pkg import BrewPkg
from genes.os.traits import get_os
from genes.process import Process


class Brew(Process):
    def __init__(self, os_name=get_os()):
        self.os_name = os_name

        if self.os_name == 'osx':
            brew_pkg = BrewPkg(os_name=self.os_name)
            if not brew_pkg.is_installed():
                brew_pkg.install()

    @staticmethod
    def run(*args, **kwargs):
        super(Brew, Brew).run('brew', *args, **kwargs)

    @staticmethod
    def install(*packages):
        Brew.run('install', *packages)

    @staticmethod
    def tap(user, repo, url=None):
        if url is None:
            Brew.run('tap', user + '/' + repo)
        else:
            Brew.run('tap', user + '/' + repo, url)

    @staticmethod
    def untap(tap):
        Brew.run('untap', tap)

    @staticmethod
    def uninstall(*packages):
        Brew.run('uninstall', *packages)

    @staticmethod
    def update():
        Brew.run('update')

    @staticmethod
    def upgrade(*packages):
        Brew.run('upgrade', *packages)

    def is_installed(self, package):
        if self.os_name != 'osx':
            return False

        response = subprocess.Popen(
                ('brew', 'ls', '--versions', package),
                stdout=subprocess.PIPE,
        ). \
            stdout. \
            read()
        return response != ''
