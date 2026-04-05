def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Anamika") # "Anamika" is an argument

# Example of a function with dictionary argument
def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Anamika", "age": 18}
my_function(my_person)

# Example of a function with list argument
def my_function(fruits):
  for fruit in fruits:
    print(fruit)
my_fruits = ["apple", "banana", "cherry","grape","orange","kiwi","mango","pineapple","strawberry","watermelon"]
my_function(my_fruits)

# Example of a function with multiple arguments
def my_function(name, age):
  print("Name:", name)
  print("Age:", age)
my_function("Anamika", 18)

# Returning a value from a function
def add(a, b):
  return a + b
result = add(5, 3)
print(result)


def concatenate(str1, str2):
  return str1 + " " + str2  
result = concatenate("Hello", "World")
print(result)

def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])
