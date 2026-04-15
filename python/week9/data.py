# 1. Create a txt file with following data.
# The txt file contains students' id, name and marks of a module.
# ID001, Harry, 85
# ID002, Bob, 78
# ID003, Shyam, 92

with open ("text.txt", "w") as file:
    data= file.write("ID001, Harry, 85\nID002, Bob, 78\nID003, Shyam, 92")
    
# 2. Read  the data and store it in a 2D list or dictionary.
# Use read function ton read the txt file and convert the required data accordingly.

def read(path): #path=text.txt
    l=[]
    with open(path) as file:
        data = file.readlines()
        print(data)
        for i in data:
            part = i.strip().split(",")
            part[2] = int(part[2])
            l.append(part)
            # print(l)
    return l
    
# student = read("text.txt")
# print(student)
# l=[1,2,3,4]
# print(l)
# for i in l:
#     print(i)

# 3. Write a function to add data in the 2D list or dictionary.
# Create a new function that takes necessary parameters and updates the 2D List.

def add(data,sid,name,mark):
    data.append([sid,name,mark])


# 4. Write a function that updates marks of students
# a. The ID of Bob needs to be taken from shell and his marks needs to br updated to 87.
# b. While taking ID and marks appropriate validation needs to be added such as:
# i. If the ID exists or not. In case of incorrect id appropriate message should be displayed.
# ii. In case of marks try expect needs to be used as marks need to be in numeric format and user may enter incorrect value or marks


def update(data):
    id=input("Enter a ID:")
    found=False
    for i in data:
        if id==i[0]:
            found=True
            try:
                mark=int(input("Enter a mark:"))
                i[2]=mark
                print("Update successfully!")
            except:
                print("Enter a numeric value!")
    if not found:
        print("ID not found!!")
        

def write(filename, data):
    with open(filename,"w") as f:
        for i in data:
            line = f"{i[0]},{i[1]},{i[2]}\n"
            f.write(line)
