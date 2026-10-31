#Check if a number is a palindrome.
num = int(input("Enter a number: "))
original_num = num
reversed_num = 0
while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
if original_num == reversed_num:
    print(f"{original_num} is a palindrome.")
else:
    print(f"{original_num} is not a palindrome.")
    

#Check if a number is an Armstrong number.
num = int(input("Enter a number: "))
order = len(str(num))
sum = 0
temp = num
while temp != 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10
if num == sum:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
    

#GCD and LCM of two numbers.
a = int(input("Enter the first number: "))  
b = int(input("Enter the second number: "))
# Function to return the GCD of two numbers
def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

# Function to return the LCM of two numbers
def lcm(x, y):
    return (x * y) // gcd(x, y)
print(f"GCD of {a} and {b} is {gcd(a, b)}")
print(f"LCM of {a} and {b} is {lcm(a, b)}")
