#!/usr/bin/env python
from typing import Callable, List, Optional, TypeVar
from genes.lib.traits import ErrorLevel
from genes.debian.traits import is_debian


T = TypeVar('T')


def is_ubuntu(versions: Optional[List[str]] = None) -> bool:
    """
    An alias for is_debian that uses Ubuntu as the distro.
    This function returns True if the OS is Ubuntu and the version is in
    the list of versions
    :param versions: a list of acceptable versions for Ubuntu.
    :return: bool, True if platform is Ubuntu.
    """
    return is_debian(versions=versions, distro_name='Ubuntu')


def run_if_ubuntu(closure: Callable[[], T],
                  error_level: ErrorLevel = ErrorLevel.warn,
                  versions: Optional[List[str]] = None) -> T:
    """
    Run a function with the args tuple as arguments if the system is Ubuntu.

    :param closure: the function to be run if the system is Ubuntu
    :param error_level: the level of error reporting to take place
    :param versions: versions of Ubuntu that are allowed; this is passed to
    is_ubuntu()
    """
    if is_ubuntu(versions=versions):
        return closure()
    elif error_level == ErrorLevel.error:
        # FIXME: logitize this
        return OSError('This command can only be run on Ubuntu')
    elif error_level == ErrorLevel.warn:
        # FIXME: should log and warn if warn
        pass
