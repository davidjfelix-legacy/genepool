from functools import wraps
import platform
from genes import debian


operating_system = platform.system()
distribution, version, codename = platform.linux_distribution()


def is_ubuntu(versions=None):
    is_version = True
    if versions:
        is_version = version in versions or codename in versions
    return operating_system == 'Linux' \
        and  distribution == 'Ubuntu' \
        and is_version


def only_ubuntu(warn=True, error=False, versions=None):
    def wrapper(func):
        @wraps(func)
        def run_if_ubuntu(*args, **kwargs):
            if is_ubuntu(versions=versions):
                return func(*args, **kwargs)
            elif error:
                # FIXME: logitize me
                raise OSError('This command can only be run on Debian')
            elif warn:
                # FIXME: should log and warn if warn
                pass

        return run_if_ubuntu
    return wrapper
