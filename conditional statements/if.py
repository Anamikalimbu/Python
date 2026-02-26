a = int(input("Enter ur age: "))
print("Your age is:", a)

if a >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
    
#conditional operators
# >, <, >=, <=, ==, !=
print(a>18)
print(a<18)
print(a>=18)
print(a<=18)
print(a==18)
print(a!=18)

#write a Program to check whether the given number is even or odd using if-else statement.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")
    