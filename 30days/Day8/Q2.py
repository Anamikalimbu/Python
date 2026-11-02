#Check if a string is a palindrome (ignore case and spaces).
def is_palindrome(s):
    # Remove spaces and convert to lowercase
    cleaned_string = ''.join(s.split()).lower()
    # Check if the cleaned string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]
print("Enter a string:")
input_string = input()
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
    