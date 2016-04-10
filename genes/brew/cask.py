from genes.process import Process


class BrewCask(Process):
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
