name = "Anamika"
age = 18

print(f"My name is {name} and I am {age} years old.")

# upper() method
print(f"My name in uppercase is {name.upper()}.")

# lower() method
print(f"My name in lowercase is {name.lower()}.")

# Multiline f-string
name = "Anamika"
score = 92

msg = f"""
Name: {name}
Score: {score}
"""
print(msg)

# Formatting numbers in f-strings
pi = 3.141592653589793
print(f"Pi rounded to 2 decimal places: {pi:.2f}")

# Using f-strings with dictionaries
person = {"name": "Anamika", "age": 18}
print(f"My name is {person['name']} and I am {person['age']} years old.")
