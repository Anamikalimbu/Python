# Remove duplicate characters, keeping the original order.
def remove_duplicates(s):
    seen = set()
    result = []
    
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    
    return ''.join(result)
# Example usage
input_string = "programming"
print(remove_duplicates(input_string))
