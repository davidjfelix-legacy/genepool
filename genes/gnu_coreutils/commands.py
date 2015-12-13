#!/usr/bin/env python
from genes.process.commands import run
from genes.posix.traits import only_posix

@only_posix()
def chgrp(path, group):
    run(['chgrp', group, path])


@only_posix()
def chown(path, user):
    run(['chown', user, path])


@only_posix()
def mkdir(path, mode=None):
    if mode:
        run(['mkdir', '-m', mode, path])
    else:
        run(['mkdir', path])


@only_posix()
def useradd():
    pass


@only_posix()
def usermod():
    pass
