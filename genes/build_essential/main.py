#!/usr/bin/env python
from genes.apt import commands as apt
from genes.debian.traits import is_debian
from genes.ubuntu.traits import is_ubuntu


def main():
    """Install packages considered necessary to build software"""
    if is_debian() or is_ubuntu():
        apt.install('build-essential')
    else:
        # FIXME: we need to support other distros soon
        pass
