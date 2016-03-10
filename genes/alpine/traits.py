from functools import wraps
from typing import List, TypeVar, Callable, Tuple, Dict
from typing import Optional

from genes.lib.logging import log_warn, log_error
from genes.lib.traits import ErrorLevel
from genes.linux.traits import get_distro, get_version, get_codename

T = TypeVar('T')


def is_alpine(versions: Optional[List[str]] = None) -> bool:
    is_version = True
    if versions:
        is_version = get_version() in versions or get_codename() in versions
    return get_distro() == 'alpine' and is_version


def only_alpine(error_level: ErrorLevel = ErrorLevel.warn, versions: Optional[List[str]] = None):
    msg = "This function can only be run in alpine"

    def wrapper(func: Callable[[Tuple, Dict], T]) -> Callable:
        @wraps
        def run_if_alpine(*args: Tuple, **kwargs: Dict) -> Optional[T]:
            if is_alpine(versions=versions):
                return func(*args, **kwargs)
            elif error_level == ErrorLevel.warn:
                log_warn(msg, func.__name__)
                return None
            elif error_level == ErrorLevel.error:
                log_error(msg, func.__name__)
                raise OSError(msg, func.__name__)
            else:
                return None

        return run_if_alpine

    return wrapper
