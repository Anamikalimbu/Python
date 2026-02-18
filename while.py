#Write a program that calculates the sum of all numbers from 1 to a given number entered by the user. The loop should stop when it reaches the number.
num = int(input("Enter a number: "))
total = 0
i = 1
while i <= num:
    total = total + i
    i = i + 1
print("The sum of all numbers from 1 to", num, "is", total)

#Write a program that uses a while loop to find the factorial of a user-inputted number
num = int(input("Enter a number: "))
factorial = 1
s = 1
while s <= num:
    factorial = factorial * s
    s = s + 1
print("The factorial of", num, "is", factorial)

#Create a program that takes an integer number from the user and prints the number in reverse using a while loop
num = int(input("Enter a number: "))
reverse = 0
while (num > 0):
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
    
print("The reverse of the number is", reverse)