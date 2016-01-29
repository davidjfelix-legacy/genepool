#!/usr/bin/env python
from typing import Callable

from .config import UserConfig
from .main import main as build


def main(config_func: Callable[[], UserConfig]) -> None:
    build(config_func)
