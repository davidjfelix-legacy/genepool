from genes.process import Process


class Brew(Process):
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

