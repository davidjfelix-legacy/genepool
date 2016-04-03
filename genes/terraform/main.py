from genes.mac.traits import is_osx

from genes.brew import brew


def main():
    if is_osx():
        brew.install()
