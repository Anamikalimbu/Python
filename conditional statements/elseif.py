#Take age as input and print child, teenager, adult or senior citizen based on the age entered by the user.
age = int(input("Enter your age: "))
if age < 13:
    print("You are a child.")
elif age >= 13 and age < 20:
    print("You are a teenager.")
elif age >= 20 and age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
    
#Write a program to check whether the given number is positive, negative or zero using if-elif-else statement.
num = int(input("Enter a number: "))
if num > 0:
    print(num, "is a positive number.")
elif num < 0:
    print(num, "is a negative number.")
else:
    print(num, "is zero.")
    
#input temperature and check whether it is hot, cold or moderate using if-elif-else statement.
temp = int(input("Enter the temperature: "))
if temp > 30:
    print("It is hot.")
elif temp >= 20 and temp <= 30:
    print("It is moderate.")
else:
    print("It is cold.")

#to convert the teamperature from Celsius to Fahrenheit and vice versa using if-elif-else statement.
temp = float(input("Enter the temperature: "))
unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ")
if unit == "C":
    fahrenheit = (temp * 9/5) + 32
    print("The temperature in Fahrenheit is:", fahrenheit)
elif unit == "F":
    celsius = (temp - 32) * 5/9
    print("The temperature in Celsius is:", celsius)
else:
    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")