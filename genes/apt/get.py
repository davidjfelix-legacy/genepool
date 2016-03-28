from invoke import task, Collection

from genes.process import Process


class APTGet(Process):
    def __init__(self):
        super(APTGet).__init__()
        self.collection = Collection('apt-get')
        self.collection.add_task(self.autoclean)
        self.collection.add_task(self.autoremove)
        self.collection.add_task(self.build_dep, 'build-dep')
        self.collection.add_task(self.check)
        self.collection.add_task(self.clean)
        self.collection.add_task(self.dist_upgrade, 'dist-upgrade')
        self.collection.add_task(self.download)
        self.collection.add_task(self.dselect_upgrade, 'dselect-upgrade')
        self.collection.add_task(self.install)
        self.collection.add_task(self.purge)
        self.collection.add_task(self.remove)
        self.collection.add_task(self.update)
        self.collection.add_task(self.upgrade)

    @task
    def run(self, cmd, **kwargs):
        super(APTGet).run('apt-get -y'.split() + cmd)

    @task
    def autoclean(self):
        self.run(['autoclean'])

    @task
    def autoremove(self):
        self.run(['autoremove'])

    @task
    def build_dep(self, *packages):
        self.run(['build-dep'] + list(packages))

    @task
    def check(self):
        self.run(['check'])

    @task
    def clean(self):
        self.run(['clean'])

    @task
    def dist_upgrade(self):
        self.run(['dist-upgrade'])

    @task
    def download(self, *packages):
        self.run(['download'] + list(packages))

    @task
    def dselect_upgrade(self):
        self.run(['dselect-upgrade'])

    @task
    def install(self, *packages):
        self.run(['install'] + list(packages))

    @task
    def purge(self, *packages):
        self.run(['purge'] + list(packages))

    @task
    def remove(self, *packages):
        self.run(['remove'] + list(packages))

    @task
    def source(self, *packages):
        self.run(['source'] + list(packages))

    @task
    def update(self):
        self.run(['update'])

    @task
    def upgrade(self):
        self.run(['upgrade'])
