# n = [1,2,3,4]
# reverse = n[::-1]
# print(reverse)

n = [1,2,3,4]
a = []
for i in range(len(n)-1, -1, -1):
    a.append(n[i])  
print(a)    
