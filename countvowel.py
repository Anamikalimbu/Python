name = input("Enter a name:")
vowels = "AEIOUaeiou"
count = 0
for char in name:
    if char in vowels:
        count += 1
print("The number of vowels in the name is:", count)