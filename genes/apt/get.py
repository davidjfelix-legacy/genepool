from genes.process import Process


class APTGet(Process):
    @staticmethod
    def run(*args, **kwargs):
        return super(APTGet, APTGet).run('apt-get', '-y', *args, **kwargs)

    @staticmethod
    def autoclean():
        APTGet.run('autoclean')

    @staticmethod
    def autoremove():
        APTGet.run('autoremove')

    @staticmethod
    def build_dep(*packages):
        APTGet.run('build-dep', *packages)

    @staticmethod
    def check():
        APTGet.run('check')

    @staticmethod
    def clean():
        APTGet.run('clean')

    @staticmethod
    def dist_upgrade():
        APTGet.run('dist-upgrade')

    @staticmethod
    def download(*packages):
        APTGet.run('download', *packages)

    @staticmethod
    def dselect_upgrade(self):
        self.run('dselect-upgrade')

    @staticmethod
    def install(*packages):
        if packages:
            APTGet.run('install', *packages)
        else:
            # FIXME: log
            raise ValueError('No packages were specified')

    @staticmethod
    def purge(*packages):
        APTGet.run('purge', *packages)

    @staticmethod
    def remove(*packages):
        APTGet.run('remove', *packages)

    @staticmethod
    def source(*packages):
        APTGet.run('source', *packages)

    @staticmethod
    def update():
        APTGet.run('update')

    @staticmethod
    def upgrade():
        APTGet.run('upgrade')
