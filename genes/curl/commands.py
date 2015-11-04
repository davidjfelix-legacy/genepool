import subprocess


def download(url, output):
    # FIXME: communicate success or failure
    subprocess.call(['curl', '-L', url, '-o', output])
