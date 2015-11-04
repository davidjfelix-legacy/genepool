#!/usr/bin/env python
import subprocess


def chgrp(path, group):
    # FIXME: don't use sudo
    subprocess.call(['chgrp', group, path])


def chown(path, user):
    # FIXME: don't use sudo
    subprocess.call(['chown', user, path])


def mkdir(path, mode=None):
    # FIXME: don't use sudo
    if mode:
        subprocess.call(['mkdir', '-m', mode, path])
    else:
        subprocess.call(['mkdir', path])
