from genes.brew import brew
from mac.traits import is_osx


def main():
    if is_osx():
        brew.install('terraform')
