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
    