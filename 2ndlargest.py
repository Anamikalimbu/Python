#Give a list of numbers and find the second largest number in the list.

numbers = [10, 20, 5, 15, 25, 30]
largest = numbers[0]
second_largest = numbers[0]
for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
print("The second largest number is:", second_largest)
