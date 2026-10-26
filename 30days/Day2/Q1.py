# Simple interest calculator (principal, rate, time).
p=float(input("Enter the principal amount: "))
r=float(input("Enter the rate of interest: "))
t=float(input("Enter the time in years: "))
simple_interest = (p * r * t) / 100 
print("Simple Interest:", simple_interest)