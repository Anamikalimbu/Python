def are_anagrams(word1, word2): 
    word1 = word1.replace(" ", "").lower()  
    word2 = word2.replace(" ", "").lower()  
    
    return sorted(word1) == sorted(word2)
first_word = input("Enter the first word: ")            
second_word = input("Enter the second word: ")
if are_anagrams(first_word, second_word):
    print("The words are anagrams.")
else:
    print("The words are not anagrams.")

# def is_anagram(word1, word2):
#     word1 = word1.lower().replace(" "," ")
#     word2 = word2.lower().replace(" ", " ")
#     return sorted(word1) == sorted(word2)

# print(is_anagram("silent","listen"))
# print(is_anagram("schoolmaster","theclassroom"))
# print(is_anagram("apple","pale"))
