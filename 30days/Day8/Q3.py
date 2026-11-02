#Capitalize the first letter of every word without using .title().
def capitalize_words(s):    
    words = s.split()
    capitalized_words = [word[0].upper() + word[1:] for word in words]
    return ' '.join(capitalized_words)
print("Enter a string:")
input_string = input()
print(capitalize_words(input_string))

#Find the longest word in a sentence.
def find_longest_word(s):
    words = s.split()
    longest_word = max(words, key=len)
    return longest_word
print("Enter a sentence:")
input_sentence = input()
print(f"The longest word is: {find_longest_word(input_sentence)}")
