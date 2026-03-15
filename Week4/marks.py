subjects = int(input("Enter number of subjects: "))

name = input("Enter student name: ")
marks = []

for i in range(subjects):
    mark = float(input(f"Subject {i+1}: "))
    marks.append(mark)

highest = max(marks)
lowest = min(marks)
total = sum(marks)
average = total / len(marks)

if average >= 90:
    grade = 'A+'
elif average >= 80:
    grade = 'A'
elif average >= 70:
    grade = 'B'
elif average >= 60:
    grade = 'C'
else:
    grade = 'F'

print("\n=== RESULTS ===")
print(f"Name: {name}")
print(f"Marks: {marks}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")
print(f"Average: {average:.1f}")
print(f"Grade: {grade}")
