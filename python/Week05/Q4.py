#add two list
a=[1,2,3,4,5,6]
b=[1,2,3,4,5,6]
c=[]
for i in range(len(a)):
    c.append(a[i]+b[i])
print(c)

#concat
n=['a','b','c','d','e']
m=['f','g','h','i','j']
r=[]
for i in range(len(n)):
    r.append(n[i]+m[i])    
print(r)
