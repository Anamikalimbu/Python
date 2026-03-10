a = int(input("Enter a 1st number"))
b = int(input("Enter a 2nd number"))
while b != 0:
    r = a%b
    a=b
    b=r
print("GCD is",a)
