import subprocess
from genes.mac import only_osx


@only_osx
def update():
    subprocess.call(['brew', 'update'])


@only_osx
def install(*packages):
    subprocess.call(['brew', 'install'] + list(packages))


@only_osx
def cask_install(*packages):
    subprocess.call(['brew', 'cask', 'install'] + list(packages))
