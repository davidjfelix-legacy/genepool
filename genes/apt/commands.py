import os
from typing import Tuple

from genes.debian.traits import is_debian
from genes.lib.logging import log_error
from genes.lib.traits import if_any_funcs
from genes.process.commands import get_env_run
from genes.ubuntu.traits import is_ubuntu


class Config:
    # FIXME: this shouldn't exist
    ENV = os.environ.copy()
    ENV['DEBIAN_FRONTEND'] = 'noninteractive'


env_run = get_env_run(Config.ENV)


@if_any_funcs(is_debian, is_ubuntu)
def install(*packages: Tuple[str, ...]) -> None:
    if packages:
        env_run('apt-get -y install'.split() + list(packages))
    else:
        msg = 'Missing packages argument'
        log_error(msg)
        raise ValueError(msg)


@if_any_funcs(is_debian, is_ubuntu)
def update() -> None:
    env_run('apt-get -y update'.split())


@if_any_funcs(is_debian, is_ubuntu)
def upgrade() -> None:
    env_run('apt-get -y upgrade'.split())


@if_any_funcs(is_debian, is_ubuntu)
def recv_keys(*keys: Tuple[str, ...]) -> None:
    if keys:
        env_run('apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys'
                .split() + list(keys))
    else:
        msg = 'Missing keys argument'
        log_error(msg)
        raise ValueError(msg)


@if_any_funcs(is_debian, is_ubuntu)
def add_repo(*line_items: Tuple[str, ...]) -> None:
    if line_items:
        env_run(['add-apt-repository', '-y', ' '.join(line_items)])
    else:
        msg = 'Missing line_items argument'
        log_error(msg)
        raise ValueError(msg)


@if_any_funcs(is_debian, is_ubuntu)
def add_ppa(ppa: str) -> None:
    if ppa:
        env_run(['add-apt-repository', '-y', 'ppa:' + ppa])
    else:
        msg = 'Missing ppa argument'
        log_error(msg)
        raise ValueError(msg)
