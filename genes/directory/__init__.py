from typing import Callable

from .config import DirectoryConfig
from .main import main as build


def main(config_func: Callable[[], DirectoryConfig]) -> None:
    build(config_func)
