from functools import wraps


def if_any(*funcs):
    def wrapper(func):
        @wraps
        def run_if_any(*args, **kwargs):
            if any([func() for func in funcs]):
                return func(*args, **kwargs)
        return run_if_any
    return wrapper
    

def if_all(*funcs):
    def wrapper(func):
        @wraps
        def run_if_all(*args, **kwargs):
            if all([fuc() for func in funcs]):
                return func(*args, **kwargs)
        return run_if_all
    return wrapper
