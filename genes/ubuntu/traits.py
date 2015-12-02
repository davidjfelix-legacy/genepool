#!/usr/bin/env python
from functools import wraps
from typing import Callable, Dict, List, Optional, Tuple, TypeVar

from genes.debian.traits import is_debian
from genes.lib.logging import log_error, log_warn
from genes.lib.traits import ErrorLevel

T = TypeVar('T')


def is_ubuntu(versions: Optional[List[str]] = None) -> bool:
    """
    An alias for is_debian that uses Ubuntu as the distro.
    This function returns True if the OS is Ubuntu and the version is in
    the list of versions
    :param versions: a list of acceptable versions for Ubuntu.
    :return: bool, True if platform is Ubuntu.
    """
    return is_debian(versions=versions, distro_name='ubuntu')


def only_ubuntu(error_level: ErrorLevel = ErrorLevel.warn, versions: Optional[List[str]] = None):
    """
    Wrap a function and only execute it if the system is ubuntu of the version specified
    :param error_level: how to handle execution for systems that aren't ubuntu
    :param versions: versions of ubuntu which are allowable
    :return: a wrapper function that wraps functions in conditional execution
    """
    msg = "This function can only be run on Ubuntu: "

    def wrapper(func: Callable[[Tuple, Dict], T]) -> Callable:
        @wraps(func)
        def run_if_ubuntu(*args: Tuple, **kwargs: Dict) -> Optional[T]:
            if is_ubuntu(versions=versions):
                return func(*args, **kwargs)
            elif error_level == ErrorLevel.warn:
                log_warn(msg, func.__name__)
                return None
            elif error_level == ErrorLevel.error:
                log_error(msg, func.__name__)
                raise OSError(msg, func.__name__)
            else:
                return None

        return run_if_ubuntu

    return wrapper
