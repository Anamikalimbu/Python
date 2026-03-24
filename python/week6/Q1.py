# matrix which are divisible by 2 and 3
# a=[[24,3,6],[8,12,18],[2,66,7]]
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         if a[i][j]%2==0 and a[i][j]%3==0:
#             print(a[i][j])
            
    
# find out  maximum and minimum element in the matrix         
# a=[[24,3,6],[8,12,18],[2,66,7]]
# max=a[0][0]
# min=a[0][0]
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         if a[i][j]>max:
#             max=a[i][j]
#         if a[i][j]<min:
#             min=a[i][j]
# print("maximum element in the matrix is ",max)
# print("minimum element in the matrix is ",min)



# a=[[24,3,6],[8,12,18],[2,66,7]]
# max=a[0][0]
# min=a[0][0]
# for i in range (len(a)):
#     for j in range(len(a[i])):
#         if a[i][j] % 2 == 0 and a[i][j] % 3 == 0:
#             print(a[i][j])
#         if a[i][j]>max:
#             max = a[i][j]
#         if a[i][j]< min:
#             min=a[i][j]
# print("maxmimu: ", max)
# print("minimum: ", min)

a=[[24,3,6],[8,12,18],[2,66,7]]
divby2and3 = []
max=a[0][0]
min=a[0][0]

for i in a:
    for j in i:
        if j%2 == 0 and j%3==0:
            divby2and3.append(j)
        if j>max:
            max=j
        if j<min:
            min=j
print(divby2and3)
print(max) 
print(min)       
