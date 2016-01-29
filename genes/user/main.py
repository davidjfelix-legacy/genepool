#!/usr/bin/env python
from typing import Callable

from genes.debian.traits import is_debian
from genes.ubuntu.traits import is_ubuntu
from .config import UserConfig


def main(config_func: Callable[[], UserConfig]):
    config = config_func()
    if is_debian() or is_ubuntu():
        pass
    else:
        pass
