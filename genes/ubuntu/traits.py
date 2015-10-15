from functools import wraps
import platform
from genes import debian


version = debian.traits.version
codename = debian.traits.codename


def is_ubuntu():
    return platform.system() == 'Linux' \
           and platform.linux_distribution == 'Ubuntu'


def only_ubuntu(warn=True, error=False, versions=None):
    def wrapper(func):
        @wraps
        def run_if_ubuntu(*args, **kwargs):
            if is_ubuntu() and versions:
                if version in versions or codename in versions:
                    return func(*args, **kwargs)
                else:
                    # FIXME: logitize me
                    raise OSError('This command can only be run on Debian {}'
                                  .format(" ".join(versions)))
            elif is_ubuntu():
                return func(*args, **kwargs)
            elif error:
                # FIXME: logitize me
                raise OSError('This command can only be run on Debian')
            else:
                # FiXME: should log and warn if warn
                pass

        return run_if_ubuntu
    return wrapper
