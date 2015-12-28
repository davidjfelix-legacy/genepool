#!/usr/bin/env python
from genes.apt import commands as apt
from genes.brew import commands as brew
from genes.debian.traits import is_debian
from genes.mac.traits import is_osx
from genes.ubuntu.traits import is_ubuntu


def main():
    if is_ubuntu() or is_debian():
        apt.update()
        apt.install('mosh')
    elif is_osx():
        brew.update()
        brew.install('mobile-shell')
    else:
        # FIXME
        pass
