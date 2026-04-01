def sum_of_evennumber(N):
    total=0
    for i in range(1,N+1):
        if i % 2 ==0:
            total +=i
    return total
N = int(input("Enter a number: "))
result = sum_of_evennumber(N)
print("The sum of even numbers from 1 to", N, "is:", result)
