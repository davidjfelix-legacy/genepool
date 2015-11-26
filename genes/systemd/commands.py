#!/usr/bin/env python
from subprocess import Popen
from typing import Tuple


def systemctl(*args: Tuple[str, ...]) -> None:
    Popen(['systemctl'] + list(args))


def disable(*services: Tuple[str, ...]) -> None:
    return systemctl('disable', *services)


def enable(*services: Tuple[str, ...]) -> None:
    return systemctl('enable', *services)


def start(*services: Tuple[str, ...]) -> None:
    return systemctl('start', *services)


def stop(*services: Tuple[str, ...]) -> None:
    return systemctl('stop', *services)


def reload(*services: Tuple[str, ...]) -> None:
    return systemctl('reload', *services)


def restart(services: Tuple[str, ...]) -> None:
    return systemctl('restart', *services)
