import os
from functools import wraps

from genes.lib.logging import log_warn, log_error
from genes.lib.traits import ErrorLevel


def is_posix() -> bool:
    """
    Determine whether the system is POSIX or not.
    :return: bool; True if the operating system is POSIX
    """
    return os.name == 'posix'


def only_posix(error_level: ErrorLevel = ErrorLevel.warn):
    """
    Wrap a function and only execute it if the system is POSIX
    :param error_level: how to handle execution for systems that aren't POSIX
    :return: a wrapper unction that wraps functions in conditional execution
    """
    msg = "This function can only be run on a POSIX system: "

    def wrapper(func):
        @wraps(func)
        def run_if_posix(*args, **kwargs):
            if is_posix():
                return func(*args, **kwargs)
            elif error_level == ErrorLevel.warn:
                log_warn(msg, func.__name__)
            elif error_level == ErrorLevel.error:
                log_error(msg, func.__name__)
                raise OSError(msg, func.__name__)
            else:
                return None

        return run_if_posix

    return wrapper
