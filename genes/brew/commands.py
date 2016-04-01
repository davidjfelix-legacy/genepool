import os
from typing import Tuple

from genes.mac.traits import only_osx
from genes.process.commands import run


class Config:
    # FIXME: this structure should not exist
    ENV = os.environ.copy()
    USER = 'splicer'
    GROUP = 'admin'


@only_osx()
def update() -> None:
    run(['brew', 'update'])


@only_osx()
def install(*packages: Tuple[str, ...]) -> None:
    run(['brew', 'install'] + list(packages))


@only_osx()
def cask_install(*packages: Tuple[str, ...]) -> None:
    run(['brew', 'cask', 'install'] + list(packages))
