print("Welcome to the menu!")
print("1. View Data")
print("2. Add Data")
print("3. Delete Data")
print("4. Exit")
while True :
    choice = int(input("Enter a number (1-4):"))
    if choice == 1:
        print("Viewing data...")
    elif choice == 2:
        print("Adding data...")
    elif choice == 3:
        print("Deleting data...")
    elif choice == 4:
        print("Exiting the program.")
        break
    else:
        print("Invalid input! Please enter a number between 1 and 4.")
