from genes.package import Package
from genes.process import Process


class Brew(Process):
    @staticmethod
    def run(*args, **kwargs):
        super(Brew).run('brew', *args)

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
    def uninstall(*args, **kwargs):
        pass

    @staticmethod
    def configure(*args, **kwargs):
        pass

    @staticmethod
    def install(*args, **kwargs):
        pass
