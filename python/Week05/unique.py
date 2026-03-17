n=[1,1,2,3,4,5,5,6,6,7,7]
a=[]
for i in range(len(n)):
    if n[i] not in a:
        a.append(n[i])
        
print(a)

# n=[1,1,2,3,4,5,5,6,6,7,7]
# a=[]
# for i in range(len(n)):
#     if n[i] in a:
#         continue
#     else:
#         a.append(n[i])
# print(a)
