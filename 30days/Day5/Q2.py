# Print the multiplication table of any number up to 10.
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)

# Factorial of n using a loop.
n = int(input("Enter a number: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print("The factorial of", n, "is:", factorial)

# Count the digits of a number.
n = int(input("Enter a number: "))
count = 0
while n > 0:
    n //= 10
    count += 1
print("The number of digits in the number is:", count)