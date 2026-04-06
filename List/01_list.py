list = ["apple", "banana", "cherry"]
print(list[1])

# Negative indexing
print(list[-1])
# Range of indexes 
list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list[2:5]) # return the items from index 2 to 4 (not including index 5)
print(list[:4]) # return the items from the beginning to index 3 (not including index 4)
print(list[3:]) # return the items from index 3 to the end of the list

list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list[-4:-1]) # return the items from index -4 to -2 (not including index -1)  


#Check if "apple" is present in the list
list = ["apple", "banana", "cherry"]
if "apple" in list:
    print("Yes, 'apple' is in the list")


#change item value
list = ["apple", "banana", "cherry"]
list[1] = "blackcurrant"
print(list)

#Insert items
list = ["apple", "banana", "cherry"]
list.insert(2, "watermelon")
print(list)

# change a range of item values
list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
list[1:3] = ["blackcurrant", "watermelon"]
print(list)

# Add items
list = ["apple", "banana", "cherry"]
list.append("orange")
print(list)

# Extend list
list = ["apple", "banana", "cherry"]
list2 = ["mango", "pineapple", "papaya"]
list.extend(list2)
print(list)

# Remove items
list = ["apple", "banana", "cherry"]
list.remove("banana")
print(list)

# Remove the last item
list = ["apple", "banana", "cherry"]
list.pop()
print(list)

# delete the first item
list = ["apple", "banana", "cherry"]
del list[0]
print(list)

# clear the list
list = ["apple", "banana", "cherry"]
list.clear()
print(list)
