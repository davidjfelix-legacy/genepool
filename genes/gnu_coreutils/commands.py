#!/usr/bin/env python

from genes.posix.traits import only_posix
from genes.process.commands import run


@only_posix()
def chgrp(path, group):
    run(['chgrp', group, path])


@only_posix()
def chown(path, user):
    run(['chown', user, path])


@only_posix()
def groupadd(*args):
    run(['groupadd'] + list(args))


@only_posix()
def ln(*args):
    run(['ln'] + list(args))


@only_posix()
def mkdir(path, mode=None):
    if mode:
        run(['mkdir', '-m', mode, path])
    else:
        run(['mkdir', path])


@only_posix()
def useradd(*args):
    # FIXME: this is a bad way to do things
    # FIXME: sigh. this is going to be a pain to make it idempotent
    run(['useradd'] + list(args))


@only_posix()
def usermod(*args):
    # FIXME: this is a bad way to do things
    run(['usermod'] + list(args))
