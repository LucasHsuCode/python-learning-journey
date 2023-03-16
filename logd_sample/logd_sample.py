from functools import wraps

def logd(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Entering function {func.__name__} with args {args} and kwargs {kwargs}")
        result = func(*args, **kwargs)
        print(f"Exiting function {func.__name__} with result {result}")
        return result
    return wrapper

@logd
def my_function(x, y):
    return x + y

result = my_function(2, 3)
print(result)