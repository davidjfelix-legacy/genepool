#!/usr/bin/env python
from genes.apt import commands as apt
from genes.debian.traits import is_debian
from genes.ubuntu.traits import is_ubuntu


def main():
    """Install uWSGI either from system package or pip"""
    # FIXME: handle pip case
    if is_ubuntu() or is_debian():
        apt.install('uwsgi')
    else:
        # FIXME: handle other distros
        pass
