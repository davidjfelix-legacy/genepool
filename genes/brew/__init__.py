import subprocess

def update():
    subprocess.call(['brew', 'update'])
    
def install(*packages):
    subprocess.call(['brew', 'install'] + packages)

def cask_install(*packages):
    subprocess.call(['brew', 'cask', 'install'] + packages)
