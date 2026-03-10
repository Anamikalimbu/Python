n = int(input("How many number do u want to input: "))
list = []
evensum = 0
oddsum = 0
while n>0:
    a = int(input("Enter a number: "))
    n = n-1
    list.append(a)
    if a % 2 == 0:
        evensum = evensum + a
    else:
        oddsum = oddsum + a
print("List ", list)
print("Even sum is", evensum)
print("Odd sum is", oddsum)
        
    
    

    
