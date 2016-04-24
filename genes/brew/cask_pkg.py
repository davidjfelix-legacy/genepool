from genes.brew.brew import Brew
from genes.os.traits import get_os
from genes.package import Package


class BrewCaskPkg(Package):
    def __init__(self, os_name=get_os()):
        self.os_name = os_name
        self.brew = Brew(os_name=self.os_name)

    def uninstall(self):
        self.brew.uninstall('brew-cask')
        self.brew.untap('caskroom/cask')

    @staticmethod
    def configure(*args, **kwargs):
        pass

    def is_installed(self):
        self.brew.is_installed('brew-cask')

    def install(self):
        self.brew.tap('caskroom', 'cask')
        self.brew.update()
        self.brew.install('brew-cask')
