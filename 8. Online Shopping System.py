products = {
    1: ("Laptop", 55000),
    2: ("Headphones", 1500),
    3: ("Keyboard", 900),
    4: ("Mouse", 600),
    5: ("USB Cable", 300)
}

cart = []

def show_products():
    print("\n===== PRODUCTS =====")

    for number, product in products.items():
        print(number, product[0], "- ₹", product[1])


def add_to_cart():
    show_products()

    choice = int(input("Enter product number: "))

    if choice not in products:
        print("Product not found!")
        return

    quantity = int(input("Enter quantity: "))

    name, price = products[choice]

    cart.append((name, price, quantity))

    print("Product added to cart!")


def checkout():
    if not cart:
        print("Cart is empty!")
        return

    total = 0

    print("\n===== SHOPPING BILL =====")

    for item in cart:
        name, price, quantity = item
        amount = price * quantity
        total += amount

        print(name, "x", quantity, "=", amount)

    discount = 0

    if total >= 50000:
        discount = total * 0.10
    elif total >= 10000:
        discount = total * 0.05

    final_amount = total - discount

    print("Total:", total)
    print("Discount:", discount)
    print("Final Amount:", final_amount)


while True:
    print("\n===== ONLINE SHOPPING =====")
    print("1. Show Products")
    print("2. Add To Cart")
    print("3. Checkout")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        show_products()
    elif choice == "2":
        add_to_cart()
    elif choice == "3":
        checkout()
    elif choice == "4":
        break
    else:
        print("Invalid choice!")
