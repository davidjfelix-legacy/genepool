from functools import wraps
import platform


version = platform.linux_distribution()[1]
codename = platform.linux_distribution()[2]


def is_debian():
    return platform.system() == 'Linux' \
           and platform.linux_distribution()[0] == 'Debian'


def only_debian(warn=True, error=False, versions=None):
    def wrapper(func):
        @wraps
        def run_if_debian(*args, **kwargs):
            if is_debian() and versions:
                if version in versions or codename in versions:
                    return func(*args, **kwargs)
                else:
                    # FIXME: logitize me
                    raise OSError('This command can only be run on Debian {}'
                                  .format(" ".join(versions)))
            elif is_debian():
                return func(*args, **kwargs)
            elif error:
                # FIXME: logitize me
                raise OSError('This command can only be run on Debian')
            else:
                # FiXME: should log and warn if warn
                pass

        return run_if_debian
    return wrapper
