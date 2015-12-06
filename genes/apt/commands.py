import os
from subprocess import Popen
from typing import Tuple

from genes.debian.traits import is_debian
from genes.lib.logging import log_error
from genes.lib.traits import if_any_funcs
from genes.ubuntu.traits import is_ubuntu


class Config:
    ENV = os.environ.copy()
    ENV['DEBIAN_FRONTEND'] = "noninteractive"


@if_any_funcs(is_debian, is_ubuntu)
def install(*packages: Tuple[str, ...]) -> None:
    if packages:
        Popen(['apt-get', '-y', 'install'] + list(packages),
              env=Config.ENV).wait()
    else:
        msg = "Missing packages argument"
        log_error(msg)
        raise ValueError(msg)


@if_any_funcs(is_debian, is_ubuntu)
def update() -> None:
    Popen(['apt-get', '-y', 'update'], env=Config.ENV).wait()


@if_any_funcs(is_debian, is_ubuntu)
def upgrade() -> None:
    Popen(['apt-get', '-y', 'upgrade'], env=Config.ENV).wait()


@if_any_funcs(is_debian, is_ubuntu)
def recv_keys(*keys: Tuple[str, ...]) -> None:
    if keys:
        Popen(
            ['apt-key', 'adv', '--keyserver',
             'hpk://pgp.mit.edu:80', '--recv-keys'] + list(keys),
            env=Config.ENV
        ).wait()
    else:
        msg = "Missing keys argument"
        log_error(msg)
        raise ValueError(msg)


@if_any_funcs(is_debian, is_ubuntu)
def add_repo(*line_items: Tuple[str, ...]) -> None:
    if line_items:
        Popen(
            ['add-apt-repository', '-y'] + [" ".join(line_items)],
            env=Config.ENV
        ).wait()
    else:
        msg = "Missing line_items argument"
        log_error(msg)
        raise ValueError(msg)


@if_any_funcs(is_debian, is_ubuntu)
def add_ppa(ppa: str) -> None:
    if ppa:
        Popen(['add-apt-repository', '-y', ppa], env=Config.ENV).wait()
    else:
        msg = "Missing ppa argument"
        log_error(msg)
        raise ValueError(msg)
