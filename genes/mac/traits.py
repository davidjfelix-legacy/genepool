import platform
from functools import wraps
from typing import Dict, List, Optional, Tuple, TypeVar
from genes.lib.logging import log_error, log_warn
from genes.lib.traits import ErrorLevel, ArgFunc2, ArgFunc, ArgFunc3

T = TypeVar('T')


def is_osx(versions: Optional[List[str]] = None) -> bool:
    """
    Determine whether the operating system is OSX or not.
    :param versions: a list of versions to return true on
    :return: bool; True if the operating system meets the above criteria
    """
    # FIXME: make version more human readable
    is_version = True
    if versions:
        is_version = platform.mac_ver()[0] in versions
    return platform.system() == 'Darwin' and is_version


def only_osx(error_level: ErrorLevel =ErrorLevel.warn,
             versions: Optional[List[str]] = None) -> ArgFunc3:
    """
    Wrap a function and only execute it if the system is OSX of the version
    specified
    :param error_level: how to handle execution for systems that aren't OSX
    :param versions: versions of OSX which are allowable
    :return: a wrapper function that wraps functions in conditional execution
    """
    msg = "This function can only be run on OSX: "

    def wrapper(func: ArgFunc) -> ArgFunc2:
        @wraps(func)
        def run_if_osx(*args: Tuple, **kwargs: Dict) -> Optional[T]:
            if is_osx(versions=versions):
                return func(*args, **kwargs)
            elif error_level == ErrorLevel.warn:
                log_warn(msg, func.__name__)
                return None
            elif error_level == ErrorLevel.error:
                log_error(msg, func.__name__)
                raise OSError(msg, func.__name__)
            else:
                return None

        return run_if_osx

    return wrapper
