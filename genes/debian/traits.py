import platform


def get_distro():
    return platform.linux_distribution()[0]


def get_version():
    """
    Get the version of the running os.
    :return: str; the version of the running os
    """
    return platform.linux_distribution()[1]


def get_codename():
    return platform.linux_distribution()[2]


def is_debian(versions=None, distro_name='Debian'):
    """
    Determine whether the operating system is debian or not.

    :param versions: a list of versions to return true on
    :type versions: list(st)
    :param distro_name: the variant/distro of debian to check for
    :type distro_name: str
    :return: bool; True if the operating system meets the above criteria
    """
    is_version = True
    if versions:
        is_version = get_version() in versions or get_codename() in versions
    return platform.system() == 'Linux' \
        and get_distro() == distro_name \
        and is_version


def run_if_debian(func, args, warn=True, error=False, versions=None):
    """
    Run a function with the args tuple as arguments if the system is Debian.

    :param func: the function to be run if the system is Debian
    :type func: Callable
    :param args: the ags to pass to func when running it
    :type args: tuple(list, map)
    :param warn: bool declaring whether or not to warn to log on non Debian
    systems
    :type warn: bool
    :param error: bool declaring whether or not to error on non Debian systems
    :type error: bool
    :param versions: versions of Debian that are allowed; this is passed to
    is_debian()
    :type versions: list(str)
    """
    if is_debian(versions=versions):
        return func(*args[0], **args[1])
    elif error:
        # FIXME: logitize this
        return OSError('This command can only be run on Debian')
    elif warn:
        # FIXME: should log and warn if warn
        pass
