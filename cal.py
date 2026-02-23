num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
# Addition
sum = num1 + num2
print("The sum of", num1, "and", num2, "is", sum)
# Subtraction   
difference = num1 - num2
print("The difference between", num1, "and", num2, "is", difference)
# Multiplication            
product = num1 * num2
print("The product of", num1, "and", num2, "is", product)
# Division
if num2 != 0:       
    quotient = num1 / num2
    print("The quotient of", num1, "divided by", num2, "is", quotient)
else:
    print("Division by zero is not allowed.")

# Modulus
if num2 != 0:
    modulus = num1 % num2
    print("The modulus of", num1, "and", num2, "is", modulus)       
else:
    print("Modulus by zero is not allowed.")    

# Exponentiation
power = num1 ** num2    
print(num1, "raised to the power of", num2, "is", power)

# Floor Division
if num2 != 0:
    floor_division = num1 // num2
    print("The floor division of", num1, "by", num2, "is", floor_division)
else:
    print("Floor division by zero is not allowed.")

    