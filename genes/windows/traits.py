import platform
from functools import wraps

# FIXME: support version strings better here. They're not human friendly
# currently. For example, Windows 10 is '10.0.10240' != '10.0'
operating_system = platform.system()
version = platform.win32_ver()[0]


def is_windows(versions=None):
    is_version = True
    if versions:
        is_version = version in versions
    return operating_system == 'Windows' and is_version


def only_windows(warn=True, error=False, versions=None):
    def wrapper(func):
        @wraps(func)
        def run_if_windows(*args, **kwargs):
            if is_windows(versions=versions):
                return func(*args, **kwargs)
            elif error:
                # FIXME: logitize me
                raise OSError('This command can only be run on Windows')
            elif warn:
                # FIXME: should log and warn if warn
                pass

        return run_if_windows

    return wrapper
