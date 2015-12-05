#!/usr/bin/env python
from enum import Enum
from functools import wraps
from typing import Callable, Dict, Optional, Tuple, TypeVar
from .logging import log_error, log_warn

T = TypeVar('T')
Closure = Callable[[], T]
BoolClosure = Callable[[], bool]
ArgFunc = Callable[[Tuple, Dict], T]
ArgFunc2 = Callable[[Tuple, Dict], ArgFunc]
ArgFunc3 = Callable[[Tuple, Dict], ArgFunc2]


class ErrorLevel(Enum):
    none = 1
    error = 2
    warn = 3


def if_any_conds(*conds: Tuple[bool, ...],
                 error_level: ErrorLevel = ErrorLevel.warn) -> ArgFunc3:
    """
    Wrap a function and only execute it if one of any of the condition
    parameters are true
    :param conds: the conditions to test for truth
    :param error_level: how to handle execution for systems that don't qualify
    :return: a wrapper function that wraps functions in conditional execution
    """
    msg = "This function: {0} was not run because none of the following " \
          "conditions were True: {1}"

    def wrapper(func: ArgFunc) -> ArgFunc2:
        @wraps(func)
        def run_if_any_conds(*args: Tuple, **kwargs: Dict) -> Optional[T]:
            if any(conds):
                return func(*args, **kwargs)
            elif error_level == ErrorLevel.warn:
                log_warn(msg.format(func.__name__, " ".join(
                    [_cond.__name__ for _cond in conds])))
                return None
            elif error_level == ErrorLevel.error:
                log_error(msg.format(func.__name__, " ".join(
                    [_cond.__name__ for _cond in conds])))
                raise ValueError(msg.format(func.__name__, " ".join(
                    [_cond.__name__ for _cond in conds])))
            else:
                return None

        return run_if_any_conds

    return wrapper


def if_any_funcs(*funcs: Tuple[BoolClosure, ...],
                 error_level: ErrorLevel = ErrorLevel.warn) -> ArgFunc3:
    """
    Wrap a function and only execute it if one of any of the function
    parameters are true
    :param funcs: the functions to run and test for truth
    :param error_level: how to handle execution for systems that don't qualify
    :return: a wrapper function that wraps functions in conditional execution
    """
    msg = "This function: {0} was not run because none of the following " \
          "functions returned True: {1}"

    def wrapper(func: ArgFunc) -> ArgFunc2:
        @wraps(func)
        def run_if_any_funcs(*args: Tuple, **kwargs: Dict) -> Optional[T]:
            if any([_func() for _func in funcs]):
                return func(*args, **kwargs)
            elif error_level == ErrorLevel.warn:
                log_warn(msg.format(func.__name__, " ".join(
                    [_func.__name__ for _func in funcs])))
                return None
            elif error_level == ErrorLevel.error:
                log_error(msg.format(func.__name__, " ".join(
                    [_func.__name__ for _func in funcs])))
                raise ValueError(msg.format(func.__name__, " ".join(
                    [_func.__name__ for _func in funcs])))
            else:
                return None

        return run_if_any_funcs

    return wrapper


def if_all_conds(*conds: Tuple[bool, ...],
                 error_level: ErrorLevel = ErrorLevel.warn) -> ArgFunc3:
    """
    Wrap a function and only execute it if all of the condition parameters are
    true
    :param conds: the conditions to test for truth
    :param error_level: how to handle execution for systems that don't qualify
    :return: a wrapper function that wraps functions in conditional execution
    """
    msg = "This function: {0} was not run because one of the following " \
          "conditions was False: {1}"

    def wrapper(func: ArgFunc) -> ArgFunc2:
        @wraps(func)
        def run_if_all_conds(*args: Tuple, **kwargs: Dict) -> Optional[T]:
            if all(conds):
                return func(*args, **kwargs)
            elif error_level == ErrorLevel.warn:
                log_warn(msg.format(func.__name__, " ".join(
                    [_cond.__name__ for _cond in conds])))
                return None
            elif error_level == ErrorLevel.error:
                log_error(msg.format(func.__name__, " ".join(
                    [_cond.__name__ for _cond in conds])))
                raise ValueError(msg.format(func.__name__, " ".join(
                    [_cond.__name__ for _cond in conds])))
            else:
                return None

        return run_if_all_conds

    return wrapper


def if_all_funcs(*funcs: Tuple[BoolClosure, ...],
                 error_level: ErrorLevel = ErrorLevel.warn) -> ArgFunc3:
    """
    Wrap a function and only execute it if all of the condition parameters are
    true
    :param funcs: the functions to run  and test for truth
    :param error_level: how to handle execution for systems that don't qualify
    :return: a wrapper function  that wraps functions in  conditional execution
    """
    msg = "This function: {0} was not run because one of the following " \
          "functions returned False: {1}"

    def wrapper(func: ArgFunc) -> ArgFunc2:
        @wraps(func)
        def run_if_all_funcs(*args: Tuple, **kwargs: Dict) -> Optional[T]:
            if all([_func() for _func in funcs]):
                return func(*args, **kwargs)
            elif error_level == ErrorLevel.warn:
                log_warn(msg.format(func.__name__, " ".join(
                    [_func.__name__ for _func in funcs])))
                return None
            elif error_level == ErrorLevel.error:
                log_error(msg.format(func.__name__, " ".join(
                    [_func.__name__ for _func in funcs])))
                raise ValueError(msg.format(func.__name__, " ".join(
                    [_func.__name__ for _func in funcs])))
            else:
                return None

        return run_if_all_funcs

    return wrapper
