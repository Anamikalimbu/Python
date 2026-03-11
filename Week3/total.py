subtotal = 0
while True:
    name = input("Enter name of product: ")
    price = float(input("Enter the price of product: "))
    
    if price < 0:
        print("Negative price skipped")
    else:
        subtotal = subtotal + price
    choice = input("Do you want to add another product? (Yes/NO): ").lower()
    
    if choice == "no":
        break

tax = subtotal * 0.13
total = subtotal + tax

delivery = input("Do you want delivery? (Yes/No): ").lower()

if delivery == "yes":
    total = total + 100
    
print("Subtotal: ", subtotal)
print("Tax(13%): ", tax)
print("Total: ", total)