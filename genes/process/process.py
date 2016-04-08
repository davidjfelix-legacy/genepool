from subprocess import Popen


class Process(object):
    @staticmethod
    def run(*args, **kwargs):
        # Popen takes a list for its command
        return Popen(args, **kwargs).wait()
