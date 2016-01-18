#!/usr/bin/env python
from .config import config


def main():
    from .main import main as install
    install(config)
