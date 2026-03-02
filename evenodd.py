#write a program that asks the user for a number and determines if it is even or odd.

number = int(input("Enter a number: "))
if number % 2 == 0:
    print(number, "is an even number.")
else:
    print(number, "is an odd number.")
