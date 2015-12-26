#!/usr/bin/env python
from functools import wraps
from typing import Callable, Dict, List, Optional, Tuple, TypeVar

from genes.lib.logging import log_error, log_warn
from genes.lib.traits import ErrorLevel
from genes.linux.traits import only_linux, get_distro, get_codename, \
    get_version

T = TypeVar('T')


@only_linux()
def is_debian(versions: Optional[List[str]] = None,
              distro_name: str = 'debian') -> bool:
    """
    Determine whether the operating system is debian or not.
    :param versions: a list of versions to return true on
    :param distro_name: the variant/distro of debian to check for
    :return: bool; True if the operating system meets the above criteria
    """
    # TODO: make this runnable for non-linux also
    is_version = True
    if versions:
        is_version = get_version() in versions or get_codename() in versions
    return get_distro() == distro_name and is_version


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
