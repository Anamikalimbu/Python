# Take a 3-digit number and print the sum of its digits using only arithmetic (// and %)
n = int(input("Enter a 3-digit number: "))
digit1 = n // 100
digit2 = (n // 10) % 10
digit3 = n % 10
sum_of_digits = digit1 + digit2 + digit3
print("Sum of digits:", sum_of_digits)
