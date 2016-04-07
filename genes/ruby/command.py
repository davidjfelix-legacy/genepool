from genes.process import Process


class Ruby(Process):
    @staticmethod
    def run(*args, **kwargs):
        super(Ruby).run('ruby', *args, **kwargs)
