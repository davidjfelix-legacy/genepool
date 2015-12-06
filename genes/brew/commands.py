from subprocess import Popen

from genes.mac.traits import only_osx


@only_osx()
def update() -> None:
    Popen(['brew', 'update']).wait()


@only_osx()
def install(*packages) -> None:
    Popen(['brew', 'install'] + list(packages)).wait()


@only_osx()
def cask_install(*packages) -> None:
    Popen(['brew', 'cask', 'install'] + list(packages)).wait()
