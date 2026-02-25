name = input("Enter customer name:")
unit = int(input("Enter units consumed:"))
cost = float(input("Enter a cost per unit:"))

total = unit * cost
tax = total * 0.08

print("---------------------------")
print("Customer name: ",name)
print("Total bill amount:",total)
print("Tax:", tax)
print("---------------------------")
