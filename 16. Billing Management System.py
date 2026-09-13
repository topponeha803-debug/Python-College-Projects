items = []

def add_item():
    name = input("Enter Item Name: ")

    price = float(input("Enter Price: "))

    quantity = int(input("Enter Quantity: "))

    if price <= 0 or quantity <= 0:
        print("Invalid price or quantity!")
        return

    items.append({
        "name": name,
        "price": price,
        "quantity": quantity
    })

    print("Item added!")


def generate_bill():
    if not items:
        print("No items added!")
        return

    subtotal = 0

    print("\n========== BILL ==========")

    for item in items:

        amount = item["price"] * item["quantity"]

        subtotal += amount

        print(
            item["name"],
            "x",
            item["quantity"],
            "=",
            amount
        )

    gst = subtotal * 0.18

    discount = 0

    if subtotal >= 10000:
        discount = subtotal * 0.10
    elif subtotal >= 5000:
        discount = subtotal * 0.05

    final_amount = subtotal + gst - discount

    print("--------------------------")
    print("Subtotal:", subtotal)
    print("GST 18%:", round(gst, 2))
    print("Discount:", round(discount, 2))
    print("Final Amount:", round(final_amount, 2))
    print("==========================")


def clear_items():
    items.clear()
    print("All items cleared!")


while True:
    print("\n===== BILLING SYSTEM =====")
    print("1. Add Item")
    print("2. Generate Bill")
    print("3. Clear Items")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_item()
    elif choice == "2":
        generate_bill()
    elif choice == "3":
        clear_items()
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
