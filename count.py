list = [1,2,6,4,5,7,6,7,8,1,4,5]
counts = {}
for num in list:
    if num in counts:
       counts[num] +=1
    else:
        counts[num] = 1
print("Repeated number and their occurence: ")
for num, count in counts.items():
    if count > 1:
        print(num, "appears", count , "items") 