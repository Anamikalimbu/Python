#combine two list of equal length by alternatingly taking elements

n=['a','b','c']
m=[1,2,3]
r=[]

for i in range(len(n)):
    r.append(n[i])
    r.append(m[i])
print(r)


#next

b=['A','H','M']
c=['@','#','&']
a=[]

for i in range(len(b)):
    a.append(b[i])
    a.append(c[i])
print(a)
    
