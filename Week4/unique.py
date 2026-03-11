original_list=[1,1,2,3,3,4,4,5,6,5,6]

unique_list = list(set(original_list))
unique_list_Ordered = []
for item in original_list:
    if item not in unique_list_Ordered:
        unique_list_Ordered.append(item)
        
print(f"Original: {original_list}")
print(f"Unique: {unique_list_Ordered}")