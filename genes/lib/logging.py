from logging import getLogger


def log_error(*args):
    getLogger('error').log(*args)


def log_warn(*args):
    getLogger('warning').log(*args)
