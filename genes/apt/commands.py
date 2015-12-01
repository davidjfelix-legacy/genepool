import os
from genes.lib.traits import run_if_any_funcs
from genes.debian.traits import is_debian
from genes.ubuntu.traits import is_ubuntu
from subprocess import Popen
from functools import partial


# TODO: utilize functools partial to handle some of the above functionality
class Config:
    ENV = os.environ.copy()
    ENV['DEBIAN_FRONTEND'] = "noninteractive"


def install(*packages) -> None:
    if packages:
        install_func = partial(_install, *packages)
        run_if_any_funcs(install_func, is_debian, is_ubuntu)
    else:
        # FIXME: need to output failure
        pass


def _install(*packages) -> None:
    Popen(['apt-get', '-y', 'install'] + list(packages), env=Config.ENV).wait()


def update() -> None:
    run_if_any_funcs(_update, is_debian, is_ubuntu)


def _update() -> None:
    Popen(['apt-get', '-y', 'update'], env=Config.ENV).wait()


def upgrade() -> None:
    run_if_any_funcs(_upgrade, is_debian, is_ubuntu)


def _upgrade() -> None:
    Popen(['apt-get', '-y', 'upgrade'], env=Config.ENV).wait()


def recv_keys(*keys) -> None:
    if keys:
        recv_keys_func = partial(_recv_keys, *keys)
        run_if_any_funcs(recv_keys_func, is_debian, is_ubuntu)
    else:
        # FIXME: log
        pass


def _recv_keys(*keys) -> None:
    Popen(
        ['apt-key', 'adv', '--keyserver',
         'hpk://pgp.mit.edu:80', '--recv-keys'] + list(keys),
        env=Config.ENV
    ).wait()


def add_repo(*line_items) -> None:
    if line_items:
        add_repo_func = partial(_add_repo, *line_items)
        run_if_any_funcs(add_repo_func, is_debian, is_ubuntu)
    else:
        # FIXME log
        pass


def _add_repo(*line_items) -> None:
    Popen(
        ['add-apt-repository', '-y'] + [" ".join(line_items)],
        env=Config.ENV
    ).wait()


def add_ppa(ppa) -> None:
    if ppa:
        add_ppa_func = partial(_add_ppa, ppa)
        run_if_any_funcs(add_ppa_func, is_debian, is_ubuntu)
    else:
        # FIXME: log
        pass


def _add_ppa(ppa) -> None:
    Popen(['add-apt-repository', '-y', ppa], env=Config.ENV).wait()
