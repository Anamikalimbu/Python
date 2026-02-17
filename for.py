# range () function is a sequence/series of numbers.
# syntax: range(start, stop, step)

#Write a program that uses a for loop and the range() function to print the numbers from 1 to 10.

for i in range(1,11):
    print(i)
    
#Create a program that defines a list of names and uses a for loop to print each name in the list.

names=["Anamika", "Anu", "Pema", "Smriti", "Ragita", "Eve", "Neha"]
print (*names, sep=",") # *names is used to unpack the list and sep="," is used to separate the names with a comma.
for name in names:
    print(name)
    print("Length of name", len(name)) #count the number of characters in the name
    


#Write a program that asks the user for a number and then prints the multiplication table for that number (from 1 to 10) using a for loop. 
number = int(input("Enter a number: "))
print("Multiplication table for", number)
for i in range(1,11):
    p=number*i  
    print(f"{number} x {i} = {p}")

    
