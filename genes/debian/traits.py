#!/usr/bin/env python
import platform
from functools import wraps
from typing import Callable, Dict, List, Optional, Tuple, TypeVar

from genes.lib.logging import log_error, log_warn
from genes.lib.traits import ErrorLevel

T = TypeVar('T')


# FIXME: remove call to platform.linux_distribution
def get_distro() -> str:
    """
    Get the distro of the running os
    :return: str; the distro of the running os
    """
    return platform.linux_distribution()[0].lower()


# FIXME: remove call to platform.linux_distribution
def get_version() -> str:
    """
    Get the version of the running os
    :return: str; the version of the running os
    """
    return platform.linux_distribution()[1].lower()


# FIXME: remove call to platform.linux_distribution
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


def only_debian(error_level: ErrorLevel = ErrorLevel.warn,
                versions: Optional[List[str]] = None):
    """
    Wrap a function and only execute it if the system is debian of the
    version specified
    :param error_level: how to handle execution for systems that aren't debian
    :param versions: versions of debian which are allowable
    :return: a wrapper function that wraps functions in conditional execution
    """
    msg = "This function can only be run on Debian: "

    def wrapper(func: Callable[[Tuple, Dict], T]) -> Callable:
        @wraps(func)
        def run_if_debian(*args: Tuple, **kwargs: Dict) -> Optional[T]:
            if is_debian(versions=versions):
                return func(*args, **kwargs)
            elif error_level == ErrorLevel.warn:
                log_warn(msg, func.__name__)
                return None
            elif error_level == ErrorLevel.error:
                log_error(msg, func.__name__)
                raise OSError(msg, func.__name__)
            else:
                return None

        return run_if_debian

    return wrapper
