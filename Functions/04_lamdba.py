# Lambda functions
# A lambda function is a small anonymous function that can take any number of arguments, but can only have one expression.
# The syntax of a lambda function is: lambda arguments: expression

# Example of a lambda function that adds two numbers
add = lambda x, y: x + y
print(add(5, 3))


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
