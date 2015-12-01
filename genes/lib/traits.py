#!/usr/bin/env python
from typing import Callable, Tuple, TypeVar
from enum import Enum


T = TypeVar('T')


class ErrorLevel(Enum):
    none = 1
    error = 2
    warn = 3


def run_if_any_conds(func: Callable[[], T], *conds: Tuple[bool]) -> T:
    """
    Run a function if any conditions are true
    :param func: the function to be run
    :param conds: the conditions used to determine whether or not to run the
    function
    :return: if the function is called its value is returned
    """
    if any(conds):
        return func()


def run_if_any_funcs(func: Callable[[], T], *funcs: Tuple[Callable[[], bool]]) -> T:
    """
    Run a function if any functions in a list return true
    :param func: the function to be run
    :param funcs: a list of functions which return booleans, used to determine
    whether or not to run the function
    :return: if the function is called its value is returned
    """
    if any([_func() for _func in funcs]):
        return func()


def run_if_all_conds(func: Callable[[], T], *conds: Tuple[bool]) -> T:
    """
    Run a function if all conditions are true
    :param func: the function to be run
    :param conds: a list of conditions used to determine whether or not to run
    the function
    :return: if the function is called its value is returned
    """
    if all(conds):
        return func()


def run_if_all_funcs(func: Callable[[], T], *funcs: Tuple[Callable[[], bool]]) -> T:
    """
    Run a function if all functions in a list return true
    :param func: the function to be run
    :param funcs: a list of functions which return booleans, used to determine
    whether or not to run the function
    :return: if the function is called its value is returned
    """
    if all([_func() for _func in funcs]):
        return func()
