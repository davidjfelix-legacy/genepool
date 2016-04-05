from subprocess import Popen


class Process(object):
    @staticmethod
    def run(*args, **kwargs):
        # Popen takes a list for its command
        Popen(args, **kwargs).wait()
