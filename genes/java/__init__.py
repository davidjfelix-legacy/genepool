#!/usr/bin/env python
from .config import JavaConfigurator


config = JavaConfigurator()


def main():
    from .main import main as install
    install(config)
