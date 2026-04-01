# def counts(word):
#     volews="aeiouAEIOU"
#     num_count = 0
#     c_count = 0
    
#     for char in word:
#         if char.isdigit():
#             num_count +=1
#         elif char.isalpha() and char not in volews:
#             c_count +=1
#     return num_count, c_count
# num_count, c_count = counts("Python123456")
# print("Number of digits:", num_count)
# print("Number of consonants:", c_count)


def count_vowels_and_consonants(word):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    
    for char in word:
        if char.isalpha():  
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
                
    return vowel_count, consonant_count
user_input = input("Enter a word: ")
vowels, consonants = count_vowels_and_consonants(user_input)
print(f"The number of vowels in the word is: {vowels}")     
print(f"The number of consonants in the word is: {consonants}")

