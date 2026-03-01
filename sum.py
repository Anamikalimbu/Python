#write a program that asks the user for a value and calculates the sum of all numbers from 1 to that value using a for loop.

n = int(input("Enter a number: "))
total = 0
for i in range(1, n+1):
    total = total + i
print("The sum of all numbers from 1 to", n, "is", total)
