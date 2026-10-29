#BMI calculator with category (underweight, normal, overweight, obese).
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 25:
    category = "Normal"
elif 25 <= bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"Your BMI is: {bmi:.2f}")
print(f"Category: {category}")

#Simple calculator using if/elif for + - * / (handle division by zero).
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero is not allowed."
else:
    result = "Error: Invalid operator."

print(f"The result is: {result}")

# ATM PIN check: 3 attempts allowed, then "card blocked".
correct_pin = "1234"
attempts = 0
while attempts < 3:
    entered_pin = input("Enter your ATM PIN: ")
    if entered_pin == correct_pin:
        print("PIN accepted. Access granted.")
        break
    else:
        attempts += 1
        print(f"Incorrect PIN. You have {3 - attempts} attempts left.")
if attempts == 3:
    print("Card blocked.")