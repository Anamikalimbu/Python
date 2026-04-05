def my_function():
    """This is a docstring that can be printed."""
    return True

print(my_function.__doc__) # This prints the docstring to the console


def add(a, b):
    """
    This function adds two numbers and returns the result.

    Parameters:
        a (int or float): First number
        b (int or float): Second number

    Returns:
        int or float: Sum of a and b
    """
    return a + b
print(add.__doc__)
