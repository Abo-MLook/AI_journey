import functools

def debug(func):
    @functools.wraps(func) # try print without this
    def wrapper(*args, **kwargs):
        print(f"Calling {func} with args={args} and kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper

@debug
def add(a, b):
    """ Adds two numbers together """
    return a + b

print(add.__name__)
print(add.__doc__)
