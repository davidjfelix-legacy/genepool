from genes.process import Process


class APTGet(Process):
    @staticmethod
    def run(cmd, **kwargs):
        super(APTGet).run('apt-get -y'.split() + cmd)

    @staticmethod
    def autoclean():
        APTGet.run(['autoclean'])

    @staticmethod
    def autoremove():
        APTGet.run(['autoremove'])

    @staticmethod
    def build_dep(*packages):
        APTGet.run(['build-dep'] + list(packages))

    @staticmethod
    def check():
        APTGet.run(['check'])

    @staticmethod
    def clean():
        APTGet.run(['clean'])

    @staticmethod
    def dist_upgrade():
        APTGet.run(['dist-upgrade'])

    @staticmethod
    def download(*packages):
        APTGet.run(['download'] + list(packages))

    @staticmethod
    def dselect_upgrade(self):
        self.run(['dselect-upgrade'])

    @staticmethod
    def install(*packages):
        APTGet.run(['install'] + list(packages))

    @staticmethod
    def purge(*packages):
        APTGet.run(['purge'] + list(packages))

    @staticmethod
    def remove(*packages):
        APTGet.run(['remove'] + list(packages))

    @staticmethod
    def source(*packages):
        APTGet.run(['source'] + list(packages))

    @staticmethod
    def update():
        APTGet.run(['update'])

    @staticmethod
    def upgrade():
        APTGet.run(['upgrade'])
