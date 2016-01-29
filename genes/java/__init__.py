#!/usr/bin/env python
from .config import config


def main(config_func=config):
    from .main import main as install
    install(config_func)
