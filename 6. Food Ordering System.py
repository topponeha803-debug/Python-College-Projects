menu = {
    1: ("Burger", 120),
    2: ("Pizza", 250),
    3: ("Sandwich", 100),
    4: ("French Fries", 80),
    5: ("Cold Drink", 50)
}

cart = []

def show_menu():
    print("\n===== FOOD MENU =====")

    for number, item in menu.items():
        print(number, item[0], "-", item[1])


def add_order():
    show_menu()

    choice = int(input("Enter item number: "))

    if choice not in menu:
        print("Invalid item!")
        return

    quantity = int(input("Enter quantity: "))

    name, price = menu[choice]

    cart.append({
        "name": name,
        "price": price,
        "quantity": quantity
    })

    print("Item added to cart!")


def show_bill():
    if not cart:
        print("Cart is empty!")
        return

    total = 0

    print("\n===== YOUR BILL =====")

    for item in cart:
        amount = item["price"] * item["quantity"]
        total += amount

        print(
            item["name"],
            "x",
            item["quantity"],
            "=",
            amount
        )

    print("---------------------")
    print("Total Amount:", total)


while True:
    print("\n===== FOOD ORDERING SYSTEM =====")
    print("1. Show Menu")
    print("2. Add Order")
    print("3. Show Bill")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        show_menu()
    elif choice == "2":
        add_order()
    elif choice == "3":
        show_bill()
    elif choice == "4":
        print("Thank you for ordering!")
        break
    else:
        print("Invalid choice!")
