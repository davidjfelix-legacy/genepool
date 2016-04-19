from genes.process import Process
from genes.process.commands import run


class Curl(Process):
    @staticmethod
    def download(url, output):
        # FIXME: communicate success or failure
        run(['curl', '-L', url, '-o', output])
