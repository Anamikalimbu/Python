#Find the second largest number in a list (no sorting shortcut allowed first, then try with sorted()).
def second_largest_no_sort(numbers):
    if len(numbers) < 2:
        return None  # Not enough elements for a second largest

    first = second = float('-inf')
    for number in numbers:
        if number > first:
            second = first
            first = number
        elif first > number > second:
            second = number

    return second if second != float('-inf') else None
#Example usage:
numbers = [3, 5, 1, 4, 2]
print(second_largest_no_sort(numbers)) 

# Using sorted()
def second_largest_with_sort(numbers):
    if len(numbers) < 2:
        return None  # Not enough elements for a second largest

    unique_numbers = list(set(numbers))  # Remove duplicates
    if len(unique_numbers) < 2:
        return None  # Not enough unique elements for a second largest

    unique_numbers.sort(reverse=True)
    return unique_numbers[1]    
# Example usage:
numbers = [3, 5, 1, 4, 2]
print(second_largest_with_sort(numbers))