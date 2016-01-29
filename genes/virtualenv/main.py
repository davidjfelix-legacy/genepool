#!/usr/bin/env python
from genes.apt import commands as apt
from genes.debian.traits import is_debian
from genes.ubuntu.traits import is_ubuntu


def main():
    if is_ubuntu() or is_debian():
        apt.update()
        apt.install('virtualenv')
    else:
        pass
