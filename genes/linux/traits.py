import platform
from functools import wraps
from typing import Dict, List, Optional, Tuple, TypeVar

from genes.lib.logging import log_error, log_warn
from genes.lib.traits import ErrorLevel, ArgFunc2, ArgFunc, ArgFunc3

T = TypeVar('T')


def is_linux(releases=None):
    """
    Determine whether the operating system is linux or not.
    :param releases: a list of releases to return true on
    :return: bool; True if the operating system meets the above criteria
    """
    is_release = True
    if releases:
        is_release = platform.release() in releases
    return platform.system() == 'Linux' and is_release


def only_linux(error_level: ErrorLevel = ErrorLevel.warn,
               releases: Optional[List[str]] = None) -> ArgFunc3:
    """
    Wrap a function and only execute it if the system is linux of the
    release specified
    :param error_level: how to handle execution for systems that aren't linux
    :param releases: releases of linux which are allowable
    :return: a wrapper function that wraps functions in conditional execution
    """
    msg = "This function can only be run on Linux: "

    def wrapper(func: ArgFunc) -> ArgFunc2:
        @wraps(func)
        def run_if_linux(*args: Tuple, **kwargs: Dict) -> Optional[T]:
            if is_linux(releases=releases):
                return func(*args, **kwargs)
            elif error_level == ErrorLevel.warn:
                log_warn(msg, func.__name__)
                return None
            elif error_level == ErrorLevel.error:
                log_error(msg, func.__name__)
                raise OSError(msg, func.__name__)
            else:
                return None

        return run_if_linux

    return wrapper
