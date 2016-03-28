from invoke import task, Collection
from subprocess import Popen


class Process(object):
    def __init__(self):
        self.collection = Collection('process')
        self.collection.add_task(self.run)

    @task
    def run(self, cmd, **kwargs):
        Popen(cmd, **kwargs).wait()
