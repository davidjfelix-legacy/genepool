#!/usr/bin/env python
from genes.apt import commands as apt
from genes.brew import commands as brew
from genes.ubuntu.traits import is_ubuntu
from genes.debian.traits import is_debian
from genes.mac.traits import is_osx


def main():
    if is_debian() or is_ubuntu():
        apt.update()
        apt.install('openssh-server')