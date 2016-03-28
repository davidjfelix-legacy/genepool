from invoke import task, Collection

from genes.package import Package


class DockerPkg(Package):
    class Debian:
        def __init__(self):
            self.collection = Collection('debian')

    def __init__(self):
        self.collection = Collection('docker')
        self.collection.add_task(self.configure)
        self.collection.add_task(self.install)
        self.collection.add_task(self.uninstall)

        self.debian = self.Debian()
        self.collection.add_collection(self.debian.collection)

    @task
    def configure(self):
        pass

    @task
    def install(self):
        pass

    @task
    def uninstall(self):
        pass
