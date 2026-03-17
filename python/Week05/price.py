
print("Welcome to a grocery store")

while True:
    name = input("Enter a name of item:")
    price = float(input("Enter a price of item:"))
    quantity = int(input("Enter quantity of item:"))
    if quantity < 1 or quantity > 10:
        print("Invalid quantity! Please enter a number between 1 and 10.")
        continue
    total_price = price * quantity
    vat = total_price * 0.13
    final_price = total_price + vat
    print(f"The total price for {quantity} {name}(s) is: NPR {total_price:.2f}")
    print(f"VAT (13%): NPR {vat:.2f}")
    print(f"Final Price: NPR {final_price:.2f}")
    more = input("Do you want to add more items? (yes/no): ").strip().lower()
    if more == "no":
        print("Thank you for shopping!")
        break
    
    
