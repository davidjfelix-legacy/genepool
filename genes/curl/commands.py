import subprocess

def download(url, output):
    # FIXME: communicate success or failure
    subprocess.call(['sudo', '-E','curl', '-L', url, '-o', output])
