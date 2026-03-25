a=[[1,2,3],[8,9,4],[7,6,5]]
b=[[2,7,6],[9,5,1],[4,3,8]]

diagonal = 0
above = 0
below = 0

for i in range(len(a)):
    for j in range(len(a[i])):
        if i == j:
            diagonal += a[i][j]
        elif i < j:
            above += a[i][j]
        else:
            below += a[i][j] 
print("Matrix A")   
print("Sum of diagonal elements: ", diagonal)
print("Sum of above diagonal elements: ", above)    
print("Sum of below diagonal elements: ", below)

for i in range(len(b)):
    for j in range(len(b[i])):
        if i == j:
            diagonal += b[i][j]
        elif i < j:
            above += b[i][j]
        else:
            below += b[i][j] 
print("Matrix B")     
print("Sum of diagonal elements: ", diagonal)
print("Sum of above diagonal elements: ", above)    
print("Sum of below diagonal elements: ", below)
