from logging import getLogger


def log_error(*args):
    getLogger('error').error(*args)


def log_warn(*args):
    getLogger('warning').warn(*args)
