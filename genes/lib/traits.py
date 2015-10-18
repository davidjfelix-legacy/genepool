from functools import wraps


def if_any(*conds):
    def wrapper(func):
        @wraps(func)
        def run_if_any(*args, **kwargs):
            if any(conds):
                return func(*args, **kwargs)
        return run_if_any
    return wrapper
    

def if_all(*conds):
    def wrapper(func):
        @wraps(func)
        def run_if_all(*args, **kwargs):
            if all(conds):
                return func(*args, **kwargs)
        return run_if_all
    return wrapper
