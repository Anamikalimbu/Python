n = int(input("How many number do u want to input: "))
list = []
while n>0:
    num = int(input("Enter a number: "))
    n = n-1
    list.append(num)
max=list[0]
min=list[0]

for num in list:
    if num> max:
        max = num
    if num< min:
        min = num

print("List", list)
print("Maximum", max)
print("Minimum", min)
