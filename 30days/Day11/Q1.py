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
    