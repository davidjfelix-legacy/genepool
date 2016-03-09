from typing import Callable

from genes.gnu_coreutils.commands import chgrp, chown, mkdir
from genes.posix.traits import is_posix
from .config import DirectoryConfig


def main(config_func: Callable[[], DirectoryConfig]) -> None:
    config = config_func()
    if is_posix():
        mkdir(config.path, mode=config.mode)
        chown(config.path, config.user)
        chgrp(config.path, config.group)
    else:
        # FIXME: handle this
        pass
