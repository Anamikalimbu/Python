m = int(input("Enter a number of rows(m): "))
n = int(input("Enter a number of columns(n): "))
matrix = []
for i in range (m):
    row = []
    for j in range (n):
        if i == j:
            row.append(1)
        elif i < j:
           row.append(2)
        else:
            row.append(3)
    matrix.append(row)

print("\n Generated 2D list")
for row in matrix:
    print(row)
            
