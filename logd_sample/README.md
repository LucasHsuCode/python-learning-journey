## Introduction

The logd decorator is a simple Python decorator that can be added to any function to print out information about the function's input arguments and output. This can be useful for debugging and understanding how functions are being called and what they are returning.

## Installation
There is no installation necessary for the logd decorator. Simply include the code in your Python file and you can use the decorator in your functions.
## Usage
To use the logd decorator, simply add the @logd decorator before your function definition, as shown in the example below:
```
@logd
def my_function(x, y):
    return x + y
```

When the my_function function is called, the logd decorator will print out information about the function call and its input arguments:
```
Entering function my_function with args (2, 3) and kwargs {}
Exiting function my_function with result 5
```

The logd decorator is customizable and can be modified to print out more or less information, depending on your needs.

## Contributing
If you find any issues or have suggestions for improvement, please feel free to contribute by creating a pull request on the GitHub repository.