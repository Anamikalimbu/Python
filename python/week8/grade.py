total_grade = 0
student_count = 0
with open ("grades.txt","r") as file: 
    for line in file:
        name, grade = line.strip().split(",")
        grade =int(grade)
        print(f"Name: {name}, Grade: {grade}")
        total_grade += grade
        student_count+= 1
if student_count>0:
    average = total_grade/student_count
    print(f"\nAverage grade: {average: .2f}")
    
