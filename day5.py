#String Methods
#String are immutable


name = "Anamika"
print(name)
#upper() method
print(name.upper())

#lower() method
print(name.lower())

#rstrip() method
#remove the trailing characters from the string
name1 = "Anamika!!!!!"
print(name1.rstrip("!"))

#replace() method
#replace the old string with the new string
print(name.replace("Anamika", "Smriti"))

#split() method
#split the string into a list of substrings
a = "Anamika Smriti Ragita"
print(a.split(" "))

#capitalize() method
#capitalize the first character of the string to uppercase and the rest to lowercase

b = "introduction to Python"
print(b.capitalize())

#center() method
#align the string to the center as per the specified parameter given by the user

str1 = "Welcome to the Python"
print(len(str1))
print(len(str1.center(50)))
print(str1.center(50))
print(str1.center(50, "*"))

#count() method
#count the number of occurrences of a substring in the string

str2 = "Python is a programming language. Python is easy to learn."
print(str2.count("Python"))

#endswith() method
#check if the string ends with a given value. If yes, it returns True, otherwise False.
str3 = "Hello, World!"
print(str3.endswith("!"))
print(str3.endswith("."))

#even we can check for a value in-between the string by providing start and end index positions.

str4 = "Welcome to the Python programming language."
print(str4.endswith("language.", 0, 40))

str5 = "Welcome to the Console !!!"
print(str5.endswith("to", 4, 10))

#find() method
#find the first occurrence of a substring in the string. It returns the index of the first occurrence. If the substring is not found, it returns -1.
str6 = "Python is a programming language. Python is easy to learn."
print(str6.find("Python"))
print(str6.find("Java"))

#index() method
#find the first occurrence of a substring in the string. It returns the index of the first occurrence. If the substring is not found, it raises a ValueError.
print(str6.index("language"))
#print(str6.index("Java"))

#isalnum() method
#check if all characters in the string are alphanumeric (letters and numbers). It returns True if all characters are alphanumeric, otherwise False.
str7 = "Anamika123"
print(str7.isalnum())

#isalpha() method
#check if all characters in the string are alphabetic (letters). It returns True if all characters are alphabetic, otherwise False.
str8 = "Anamika"
print(str7.isalpha())
print(str8.isalpha())

#islower() method
#check if all characters in the string are lowercase. It returns True if all characters are lowercase, otherwise False.
str9 = "hello world"
print(str9.islower())
str10 = "Hello World"
print(str10.islower())

#isprintable() method
#check if all characters in the string are printable. It returns True if all characters are printable, otherwise False.
str11 = "We wish you a Happy Holi"
print(str11.isprintable())
str12 = "We wish you a Happy Holi\n"
print(str12.isprintable())

#isspace() method
#check if all characters in the string are whitespace. It returns True if all characters are whitespace, otherwise False.

str13 = "   "
print(str13.isspace())
str14 = "  Hello  "
print(str14.isspace())

#istitle() method
#return True only if the first letter of each word of the string is capitalized and the rest are lowercase. Otherwise, it returns False.

str15 = "Welcome To The Python Programming"
print(str15.istitle())

f = "To kill a Mocking bird"
print(f.istitle())

#isupper() method
#check if all characters in the string are uppercase. It returns True if all characters are uppercase, otherwise False.
str16 = "HELLO WORLD"
print(str16.isupper())

#startswith() method
#check if the string starts with a given value. If yes, it returns True, otherwise False.
str17 = "Hello, World!"
print(str17.startswith("Hello"))

str18 = "Python is a Interpreted language."
print(str18.startswith("Python"))

#swapcase() method
#convert uppercase characters to lowercase and lowercase characters to uppercase.
print(str18.swapcase())

str19 = "welcome"
print(str19.swapcase())

#title() method
#convert the first character of each word to uppercase and the rest to lowercase.
str20 = "welcome to the python programming"
print(str20.title())