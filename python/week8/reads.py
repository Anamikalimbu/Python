with open('file.txt','r+') as file:
    print(file.read())
    file.seek(0)
    print(file.write("Start"))


# with open('file.txt','r+') as file:
#      print(file.write("Start"))
#      file.seek(0)
#      print(file.read())
     
     
