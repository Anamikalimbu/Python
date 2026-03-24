n = int(input("Enter a number of students: "))
students = {}
for i in range (n):
    name=input("Enter the name of student: ")
    marks=int(input("Enter the marks obtained by the student: "))
    students[name]=marks
print(students)
