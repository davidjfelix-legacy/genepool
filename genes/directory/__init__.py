#!/usr/bin/env python
from genes.gnu_coreutils.commands import chgrp, chown, mkdir
from genes.posix.traits import is_posix


DirectoryConfig = namedtuple('DirectoryConfig', ['path', 'mode', 'group', 'user'])


def main(config_func=None):
    if config_func:
        config = config_func()
        if is_posix():
            mkdir(config.path, mode=config.mode)
            chown(config.path, config.user)
            chgrp(config.path, config.group)
        else:
            # FIXME: handle this
            pass
    else:
        # FIXME: log incorrect use
        pass
