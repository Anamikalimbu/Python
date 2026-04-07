# ------------------------------
# Function with Docstring
# ------------------------------

def square(n):
    """
    Takes in a number n, returns the square of n

    Demonstrates a well-documented function using docstrings.

    Parameters:
        n (int): A number whose properties we explore

    Returns:
        str: A string describing the number
    """
    if n % 2 == 0:
        return f"{n} is even"
    else:
        return f"{n} is odd"


# ------------------------------
# Class with Docstring
# ------------------------------

class Programmer:
    """
    A class to represent a Programmer.

    Attributes:
        name (str): Programmer's name
        language (str): Language they code in

    Methods:
        printInfo(): Prints information about the programmer
    """
    def __init__(self, name, language):
        self.name = name
        self.language = language

    def printInfo(self):
        """Prints information about the programmer."""
        print(f"Name: {self.name}, Language: {self.language}")


# ------------------------------
# Using the function and class
# ------------------------------

print(square(7))   # Output: 7 is odd

p = Programmer("Anamika", "Python")
p.printInfo()      # Output: Name: Anamika, Language: Python

# ------------------------------
# Using help() to view docstring
# ------------------------------

help(square)
