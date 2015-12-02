import os
from functools import wraps

system = os.name


def is_posix():
    return system == 'posix'


def only_posix(warn=True, error=False):
    def wrapper(func):
        @wraps(func)
        def run_if_posix(*args, **kwargs):
            if is_posix():
                return func(*args, **kwargs)
            elif error:
                # FIXME: logitize me
                raise OSError('This command can only be run on POSIX systems')
            elif warn:
                # FIXME: should log and warn if warn
                pass

        return run_if_posix

    return wrapper
