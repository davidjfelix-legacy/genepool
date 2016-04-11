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
        if packages:
            APTGet.run('build-dep', *packages)
        else:
            # FIXME: log
            raise ValueError('No packages were specified')

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
        if packages:
            APTGet.run('download', *packages)
        else:
            # FIXME: log
            raise ValueError('No packages were specified')

    @staticmethod
    def dselect_upgrade():
        APTGet.run('dselect-upgrade')

    @staticmethod
    def install(*packages):
        if packages:
            APTGet.run('install', *packages)
        else:
            # FIXME: log
            raise ValueError('No packages were specified')

    @staticmethod
    def purge(*packages):
        if packages:
            APTGet.run('purge', *packages)
        else:
            # FIXME: log
            raise ValueError('No packages were specified')

    @staticmethod
    def remove(*packages):
        if packages:
            APTGet.run('remove', *packages)
        else:
            # FIXME: log
            raise ValueError('No packages were specified')

    @staticmethod
    def source(*packages):
        if packages:
            APTGet.run('source', *packages)
        else:
            # FIXME: log
            raise ValueError('No packages were specified')

    @staticmethod
    def update():
        APTGet.run('update')

    @staticmethod
    def upgrade():
        APTGet.run('upgrade')
