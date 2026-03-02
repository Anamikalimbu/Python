#input a string and count how many times each character appears in the string.

string = input("Enter a string: ")
char_count = {}
for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
for char, count in char_count.items():
    print( char, "appears", count)