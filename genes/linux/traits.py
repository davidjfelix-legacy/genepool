from functools import wraps
import platform


operating_system = platform.system()
release = platform.release()
distribution, version, codename = platform.linux_distribution()


def is_linux(releases=None):
    is_release = True
    if releases:
        is_release = release in releases
    return operating_system == 'Linux' and is_release


def only_linux(warn=True, error=False, releases=None):
    def wrapper(func):
        @wraps(func)
        def run_if_linux(*args, **kwargs):
            if is_linux(releases=releases):
                return func(*args, **kwargs)
            elif error:
                # FIXME: logitize me
                raise OSError('This command can only be run on Debian')
            elif warn:
                # FIXME: should log and warn if warn
                pass

        return run_if_linux
    return wrapper
