def is_palindrome(word):
    word = word.lower()  
    reversed_word = word[::-1]  
    
    if word == reversed_word:
        return True
    else:
        return False
user_word = input("Enter a word: ")
if is_palindrome(user_word):
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")

# def is_palindrome(word):
#     word = word.lower()
#     return word == word [:: -1]
# print(is_palindrome("Madam"))
# print(is_palindrome("racecar"))
# print(is_palindrome("Hello"))
