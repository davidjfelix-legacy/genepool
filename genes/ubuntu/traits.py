from genes.debian.traits import is_debian


def is_ubuntu(versions=None):
    """
    An alias for is_debian that uses Ubuntu as the distro.
    This function returns True if the OS is Ubuntu and the version is in
    the list of versions
    :param versions: a list of acceptable versions for Ubuntu.
    :type versions: list(str)
    :return: bool, True if platform is Ubuntu.
    """
    return is_debian(versions=versions, distro_name='Ubuntu')


def run_if_ubuntu(func, args, warn=True, error=False, versions=None):
    """
    Run a function with the args tuple as arguments if the system is Ubuntu.

    :param func: the function to be run if the system is Ubuntu
    :type func: Callable
    :param args: the ags to pass to func when running it
    :type args: tuple(list, map)
    :param warn: bool declaring whether or not to warn to log on non Ubuntu
    systems
    :type warn: bool
    :param error: bool declaring whether or not to error on non Ubuntu systems
    :type error: bool
    :param versions: versions of Ubuntu that are allowed; this is passed to
    is_ubuntu()
    :type versions: list(str)
    """
    if is_ubuntu(versions=versions):
        return func(*args[0], **args[1])
    elif error:
        # FIXME: logitize this
        return OSError('This command can only be run on Ubuntu')
    elif warn:
        # FIXME: should log and warn if warn
        pass
