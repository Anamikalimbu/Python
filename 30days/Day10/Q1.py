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



#Remove duplicates from a list
def remove_duplicates(numbers):
    return list(set(numbers))

# Example usage:
numbers = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(numbers))

#Rotate a list by k positions.
def rotate_list(numbers, k):
    if not numbers:
        return numbers  # Return empty list if input is empty

    k = k % len(numbers)  # Handle cases where k is greater than the length of the list
    return numbers[-k:] + numbers[:-k]
# Example usage:
numbers = [1, 2, 3, 4, 5]
k = 2
print(rotate_list(numbers, k))

#Merge two sorted lists into one sorted list
def merge_sorted_lists(list1, list2):
    merged_list = []
    i = j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # Append remaining elements from both lists
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])

    return merged_list

# Example usage:
list1 = [1, 3, 5]
list2 = [2, 4, 6]
print(merge_sorted_lists(list1, list2))
