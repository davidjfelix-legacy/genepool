from functools import wraps
from genes.debian.traits import is_debian


def is_ubuntu(versions=None):
    return is_debian(versions=versions, distro_name='Ubuntu')


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
