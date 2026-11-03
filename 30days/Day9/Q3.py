#Count the frequency of each character.
def count_frequency(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency
# Example usage
input_string = "hello"
print("Original string:", input_string)
print("Character frequencies:", count_frequency(input_string))

#Compress a string: "aaabbc" becomes "a3b2c1".
def compress_string(s):
    if not s:
        return ""
    
    compressed = []
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1] + str(count))
            count = 1
            
    compressed.append(s[-1] + str(count))  # Add the last character and its count
    return ''.join(compressed)
# Example usage
input_string = "aaabbc"
print("Original string:", input_string)
print("Compressed string:", compress_string(input_string))
