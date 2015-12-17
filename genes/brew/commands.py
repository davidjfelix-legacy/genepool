import os
from subprocess import Popen

from genes.mac.traits import only_osx
from genes.process.commands import get_env_run_as


class Config:
    ENV = os.environ.copy()
    ENV['DEBIAN_FRONTEND'] = 'noninteractive'
    USER = 'splicer'
    GROUP = 'admin'


env_run_as = get_env_run_as(Config.ENV)


@only_osx()
def update() -> None:
    env_run_as(['brew, update'], user=Config.USER, group=Config.GROUP)


@only_osx()
def install(*packages) -> None:
    Popen(['brew', 'install'] + list(packages)).wait()


@only_osx()
def cask_install(*packages) -> None:
    Popen(['brew', 'cask', 'install'] + list(packages)).wait()
