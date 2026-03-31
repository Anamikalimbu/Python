# def twoSum(nums, target):
#     seen = {}  
    
#     for i, num in enumerate(nums):
#         diff = target - num
        
#         if diff in seen:
#             return [seen[diff], i]
        
#         seen[num] = i

# nums = [2, 7, 11, 15]
# target = 9
# print(twoSum(nums, target))  

def twoSum(nums, target):
    n = len(nums)
    
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]


nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))   
