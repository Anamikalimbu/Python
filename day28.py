# Day 28 - f-strings in Python

name = "Anamika"
country = "Nepal"
age = 18

# Basic f-string
print(f"Hello, my name is {name}")
print(f"I am from {country} and I am {age} years old")

# Expressions inside f-strings
print(f"Sum of 5 and 6 is {5 + 6}")
print(f"Value of 5^2 is {5 ** 2}")
print(f"Is age > 18? {age > 18}")

# Calling methods inside f-strings
friends = ["Smriti", "Ragita", "Neha"]
print(f"Friends list: {friends}")
print(f"First friend: {friends[0]}")
print(f"Name in uppercase: {name.upper()}")

# Formatting numbers
pi = 3.14159265
print(f"Value of pi: {pi}")
print(f"Value of pi (2 decimal): {pi:.2f}")
print(f"Value of pi (4 decimal): {pi:.4f}")

# Padding and alignment
item = "Apple"
price = 1.5
print(f"|{item:<10}|{price:>10}|")   # Left and right align
print(f"|{item:^10}|{price:^10}|")   # Center align

# Multiline f-string
message = (
    f"Name: {name}\n"
    f"Age: {age}\n"
    f"Country: {country}"
)
print(message)
