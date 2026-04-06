# Loop in list
list = ["apple", "banana", "cherry"]
for x in list:
    print(x)
    
# Loop through the index numbers
list = ["apple", "banana", "cherry"]
for i in range(len(list)):
    print(list[i])

# Using a while loop
list = ["apple", "banana", "cherry"]
i = 0
while i < len(list):
    print(list[i])
    i = i + 1
    
# Looping using list comprehension
list = ["apple", "banana", "cherry"]
[print(x) for x in list]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# List comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

print(newlist)

# syntax: newlist = [expression for item in iterable if condition == True]
