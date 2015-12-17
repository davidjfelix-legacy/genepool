from genes.process.commands import run


def download(url, output):
    # FIXME: communicate success or failure
    run(['curl', '-L', url, '-o', output])
