#!/usr/bin/env python
import subprocess
from genes.posix.traits import only_posix


@only_posix
def chgrp(path, group):
    # FIXME: don't use sudo
    subprocess.call(['chgrp', group, path])


@only_posix
def chown(path, user):
    # FIXME: don't use sudo
    subprocess.call(['chown', user, path])


@only_posix
def mkdir(path, mode=None):
    # FIXME: don't use sudo
    if mode:
        subprocess.call(['mkdir', '-m', mode, path])
    else:
        subprocess.call(['mkdir', path])
