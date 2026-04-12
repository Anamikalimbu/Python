with open("password.txt", "r") as file:
    lines = file.readlines()
    nums=[1,2,3,4,5,6,7,8,9,0]
    chars=["@","#","$","%","&","*"]
    weak=[]
    for line in lines:
        password = line.strip()
        if any(str(char) in password for char in nums) and any(sign in password for sign in chars) and (len(password)>=8):
            print("This password is strong",password)
        else:
            week.append(password)
with open("weak.txt","w") as file:
    for pwd in weak:
        file.write(f"{pwd}\n")
            
