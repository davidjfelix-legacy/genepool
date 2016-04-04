from genes.mac.traits import is_osx

from genes.brew.command import Brew


def main():
    if is_osx():
        brew = Brew()
        brew.install()
