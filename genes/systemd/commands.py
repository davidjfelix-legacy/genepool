#!/usr/bin/env python
from subprocess import Popen
from typing import List


def systemctl(*args: List[str]):
    Popen(['systemctl'] + list(args))


def start(service: str):
    systemctl('start', service)


def stop(service: str):
    systemctl('stop', service)


def restart(service: str):
    systemctl('restart', service)


def reload(service: str):
    systemctl('reload', service)
