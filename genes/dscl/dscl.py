from genes.process import Process


class DSCL(Process):
    def __init__(self, data_source='.'):
        self.data_source = data_source

    @staticmethod
    def run(*args, **kwargs):
        return super(DSCL, DSCL).run('dscl', *args, **kwargs)

    def create(self, *args):
        DSCL.run(self.data_source, '-create', *args)
