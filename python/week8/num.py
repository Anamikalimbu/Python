# numbers=[]
# with open('lab8.txt','r') as file:
#     for line in file:
#         parts= line.split(",")
#         for n in parts:
#             numbers.append(int(n))
# if numbers:
#     print(f"Sum: {sum(numbers)}")
#     print(f"Maximum: {max(numbers)}")
#     print(f"Minimum: {min(numbers)}")
# else:
#     print("No numbers found in the file.")

with open("lab8.txt", "r") as file:
    lines = file.readlines()
    sum = 0
    for line in lines:
        numbers = line.strip().split(",")
        for nums in numbers:
            sum+=int(nums)
    print(sum)
    