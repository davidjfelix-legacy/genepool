#!/usr/bin/env python
import platform
from typing import Callable, List, Optional, TypeVar
from genes.lib.traits import ErrorLevel
from genes.lib.logging import log_error, log_warning


T = TypeVar('T')


def get_distro() -> str:
    """
    Get the distro of the running os

    :return: str; the distro of the running os
    """
    return platform.linux_distribution()[0].lower()


def get_version() -> str:
    """
    Get the version of the running os

    :return: str; the version of the running os
    """
    return platform.linux_distribution()[1].lower()


def get_codename() -> str:
    """
    Ge the codename of the running os.

    :return: str; the codename of the running os
    """
    return platform.linux_distribution()[2].lower()


def is_debian(versions: Optional[List[str]] = None,
              distro_name: str = 'debian') -> bool:
    """
    Determine whether the operating system is debian or not.

    :param versions: a list of versions to return true on
    :param distro_name: the variant/distro of debian to check for
    :return: bool; True if the operating system meets the above criteria
    """
    is_version = True
    if versions:
        is_version = get_version() in versions or get_codename() in versions
    return platform.system().lower() == 'linux' \
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
    error = 'This command can only be run on Debian: run_if_debian'
    if is_debian(versions=versions):
        return closure()
    elif error_level == ErrorLevel.error:
        log_error(error, str(closure))
        return OSError(error, str(closure))
    elif error_level == ErrorLevel.warn:
        log_warning(error, str(closure))
