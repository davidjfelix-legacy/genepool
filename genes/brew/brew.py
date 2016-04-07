import shutil

from genes.curl.commands import download
from genes.package import Package
from genes.process import Process
from genes.ruby.command import Ruby


class Brew(Process):
    @staticmethod
    def run(*args, **kwargs):
        super(Brew).run('brew', *args, **kwargs)

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
    def update():
        Brew.run('update')

    @staticmethod
    def upgrade(*packages):
        Brew.run('upgrade', *packages)


class BrewPkg(Package):
    @staticmethod
    def is_installed():
        return shutil.which("brew") is not None

    @staticmethod
    def uninstall(*args, **kwargs):
        if BrewPkg.is_installed():
            download(
                    'https://raw.githubusercontent.com/Homebrew/install/master/uninstall',
                    '/tmp/brew_uninstall'
            )
            ruby = Ruby()
            ruby.run('-e', '/tmp/brew_uninstall')

    @staticmethod
    def configure(*args, **kwargs):
        pass

    @staticmethod
    def install(*args, **kwargs):
        if not BrewPkg.is_installed():
            download(
                    'https://raw.githubusercontent.com/Homebrew/install/master/install',
                    '/tmp/brew_install'
            )
            ruby = Ruby()
            ruby.run('-e', '/tmp/brew_install')
