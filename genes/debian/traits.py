#!/usr/bin/env python
import platform
from typing import Callable, List, Optional, TypeVar
from genes.lib.traits import ErrorLevel


T = TypeVar('T')


def get_distro() -> str:
    """
    Get the distro of the running os

    :return: str; the distro of the running os
    """
    return platform.linux_distribution()[0]


def get_version() -> str:
    """
    Get the version of the running os

    :return: str; the version of the running os
    """
    return platform.linux_distribution()[1]


def get_codename() -> str:
    """
    Ge the codename of the running os.

    :return: str; the codename of the running os
    """
    return platform.linux_distribution()[2]


def is_debian(versions: Optional[List[str]] = None,
              distro_name: str = 'Debian') -> bool:
    """
    Determine whether the operating system is debian or not.

    :param versions: a list of versions to return true on
    :param distro_name: the variant/distro of debian to check for
    :return: bool; True if the operating system meets the above criteria
    """
    is_version = True
    if versions:
        is_version = get_version() in versions or get_codename() in versions
    return platform.system() == 'Linux' \
        and get_distro() == distro_name \
        and is_version


def run_if_debian(closure: Callable[[], T],
                  error_level: ErrorLevel = ErrorLevel.warn,
                  versions: Optional[List[str]] = None):
    """
    Run a function with the args tuple as arguments if the system is Debian.

    :param closure: the function to be run if the system is Debian
    :param error_level: the level of error reporting to take place
    :param versions: versions of Debian that are allowed; this is passed to
    is_debian()
    """
    if is_debian(versions=versions):
        return closure()
    elif error_level == ErrorLevel.error:
        # FIXME: logitize this
        return OSError('This command can only be run on Debian')
    elif error_level == ErrorLevel.warn:
        # FIXME: should log and warn if warn
        pass
