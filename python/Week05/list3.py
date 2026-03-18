# even position of the list
list = [43,23,21,44,56,75]
even_position = []
for i in range(len(list)):
    if i%2==1:
        even_position.append(list[i])   
print(even_position)

#odd position of the list
n = [12,22,32,42,52,62]
odd_position = []
for i in range(len(n)):
    if i%2==0:
        odd_position.append(n[i])
print(odd_position)
