
items = []
prices = []
quantities = []

print("=== Shopping Cart (NPR) ===")

while True:
    item_name = input("Enter item name: ").strip()
    
    price = float(input("Enter price per item: NPR "))
    
    quantity = int(input("Enter quantity: "))
    
    items.append(item_name)
    prices.append(price)
    quantities.append(quantity)
    
    add_more = input("\nDo you want to add another item? (yes/no): ").strip().lower()
    
    if add_more == "no":
        break

print("\n=== Receipt (NPR) ===")
print("-" * 40)

subtotal = 0
vat_rate = 0.13  # 13% VAT

for i in range(len(items)):
    item_total = prices[i] * quantities[i]
    subtotal += item_total
    print(f"{items[i]:<20} x{quantities[i]:<3} @ NPR{prices[i]:<8.2f} = NPR{item_total:.2f}")

print("-" * 40)

print(f"{'Subtotal':<30} NPR{subtotal:.2f}")

vat_amount = subtotal * vat_rate
print(f"{'VAT (13%)':<30} NPR{vat_amount:.2f}")

final_total = subtotal + vat_amount
print("-" * 40)
print(f"{'TOTAL':<30} NPR{final_total:.2f}")

print("\nThank you for shopping!")
