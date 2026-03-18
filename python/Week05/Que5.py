#implement bubble sort algorithm for sorting a list of numbers in ascending order
a=[5,2,9,1,5,6]
for i in range(len(a)-1):
    for j in range(len(a)-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(a)

#descending order
a=[5,2,9,1,5,6]
for i in range(len(a)-1):
    for j in range(len(a)-1):
        if a[j] < a[j+1]:
            a[j], a[j+1] = a[j+1], a[j] 
print(a)
