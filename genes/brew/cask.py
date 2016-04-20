from genes.brew.cask_pkg import BrewCaskPkg
from genes.os.traits import get_os
from genes.process import Process


class BrewCask(Process):
    def __init__(self, os_name=None):
        self.os_name = os_name if os_name else get_os()

        if os_name == 'osx':
            brew_cask_pkg = BrewCaskPkg(os_name=self.os_name)
            if not brew_cask_pkg.is_installed():
                brew_cask_pkg.install()

    @staticmethod
    def run(*args, **kwargs):
        super(BrewCask, BrewCask).run('brew', 'cask', *args, **kwargs)

    @staticmethod
    def install(*packages):
        BrewCask.run('install', *packages)

    @staticmethod
    def uninstall(*packages):
        BrewCask.run('uninstall', *packages)

    @staticmethod
    def update():
        BrewCask.run('update')
