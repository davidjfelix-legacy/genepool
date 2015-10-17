from functools import wraps
import platform


operating_system = platform.system()
distribution, version, codename = platform.linux_distribution()


def is_debian(versions=None):
    is_version = True
    if versions:
        is_version = version in versions or codename in versions
    return operating_system == 'Linux' \
        and distribution == 'Debian' \
        and is_version


def only_debian(warn=True, error=False, versions=None):
    def wrapper(func):
        @wraps
        def run_if_debian(*args, **kwargs):
            if is_debian(versions=versions):
                return func(*args, **kwargs)
            elif error:
                # FIXME: logitize me
                raise OSError('This command can only be run on Debian')
            elif warn:
                # FIXME: should log and warn if warn
                pass

        return run_if_debian
    return wrapper
