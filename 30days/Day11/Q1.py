#Two Sum: find a pair that adds to a target (brute force first).
def two_sum_brute_force(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i, j]
    return None

#Example usage:
numbers = [2, 7, 11, 15]
target = 9
result = two_sum_brute_force(numbers, target)
if result:
    print(f"Pair found at indices: {result}")
else:
    print("No pair found.")

#Find the missing number in a list containing 1..n
def find_missing_number(numbers):
    n = len(numbers) + 1  # Since one number is missing, the total count should be n
    expected_sum = n * (n + 1) // 2  # Sum of first n natural numbers
    actual_sum = sum(numbers)
    return expected_sum - actual_sum

# Example usage:
numbers = [1, 2, 4, 5, 6]
print(find_missing_number(numbers))