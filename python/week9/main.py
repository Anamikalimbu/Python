import data 
students=data.read("text.txt")
print(students)

data.add(students, "ID004","Anamika",87)
print(students)

data.update(students)
data.write("text.txt",students)
