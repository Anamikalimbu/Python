subtotal = 0
while True:
    name = input("Enter name of product: ")
    price = float(input("Enter the price of product: "))
    
    total = subtotal + price
    
    choice = input("Do you want to add another product? (Yes/NO): ").lower()
    
    if choice == "no":
        break
print("Your total shopping amount is: ", total)

    

