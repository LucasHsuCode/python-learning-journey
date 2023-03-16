from functools import wraps

def logd(func):
    """
    A decorator that adds logging functionality to the decorated function. When the decorated function is called,
    the decorator will print a message indicating that the function is being entered, and another message indicating
    that the function is being exited. The decorator also uses the `wraps` function from the `functools` module to
    ensure that the decorated function retains its original name and docstring.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: The decorated function.

    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        The wrapper function that is returned by the `logd` decorator. This function will log a message indicating
        that the decorated function is being entered, call the decorated function with the given arguments, log a
        message indicating that the decorated function is being exited, and then return the result of the decorated
        function.

        Args:
            *args: Positional arguments to be passed to the decorated function.
            **kwargs: Keyword arguments to be passed to the decorated function.

        Returns:
            Any: The result of the decorated function.

        """
        print(f"Entering function {func.__name__} with args {args} and kwargs {kwargs}")
        result = func(*args, **kwargs)
        print(f"Exiting function {func.__name__} with result {result}")
        return result
    return wrapper

@logd
def my_function(x, y):
    """
    A function that adds two numbers together.

    Args:
        x (int): The first number.
        y (int): The second number.

    Returns:
        int: The sum of `x` and `y`.

    """
    return x + y

result = my_function(2, 3)
print(result)