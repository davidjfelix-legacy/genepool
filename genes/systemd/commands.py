#!/usr/bin/env python
from subprocess import Popen
from typing import Tuple

from genes.linux.traits import only_linux


@only_linux()
def systemctl(*args: Tuple[str, ...]) -> None:
    Popen(['systemctl'] + list(args))


@only_linux()
def disable(*services: Tuple[str, ...]) -> None:
    return systemctl('disable', *services)


@only_linux()
def enable(*services: Tuple[str, ...]) -> None:
    return systemctl('enable', *services)


@only_linux()
def start(*services: Tuple[str, ...]) -> None:
    return systemctl('start', *services)


@only_linux()
def stop(*services: Tuple[str, ...]) -> None:
    return systemctl('stop', *services)


@only_linux()
def reload(*services: Tuple[str, ...]) -> None:
    return systemctl('reload', *services)


@only_linux()
def restart(services: Tuple[str, ...]) -> None:
    return systemctl('restart', *services)
