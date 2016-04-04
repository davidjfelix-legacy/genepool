from subprocess import Popen


class Process(object):
    @staticmethod
    def run(cmd, **kwargs):
        Popen(cmd, **kwargs).wait()
