cars = {
    1: {"name": "Swift", "price": 1500, "available": True},
    2: {"name": "Creta", "price": 2500, "available": True},
    3: {"name": "Thar", "price": 3000, "available": True},
    4: {"name": "Fortuner", "price": 5000, "available": True}
}

def show_cars():
    print("\n===== AVAILABLE CARS =====")

    for number, car in cars.items():
        status = "Available" if car["available"] else "Rented"

        print(
            number,
            car["name"],
            "- ₹",
            car["price"],
            "per day -",
            status
        )


def rent_car():
    show_cars()

    choice = int(input("Select car: "))

    if choice not in cars:
        print("Invalid car!")
        return

    car = cars[choice]

    if not car["available"]:
        print("Car is already rented!")
        return

    name = input("Enter customer name: ")
    days = int(input("Enter number of days: "))

    amount = car["price"] * days

    car["available"] = False

    print("\n===== RENTAL DETAILS =====")
    print("Customer:", name)
    print("Car:", car["name"])
    print("Days:", days)
    print("Total Rent: ₹", amount)


def return_car():
    show_cars()

    choice = int(input("Enter returned car number: "))

    if choice in cars:
        cars[choice]["available"] = True
        print("Car returned successfully!")
    else:
        print("Invalid car!")


while True:
    print("\n===== CAR RENTAL SYSTEM =====")
    print("1. Show Cars")
    print("2. Rent Car")
    print("3. Return Car")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        show_cars()
    elif choice == "2":
        rent_car()
    elif choice == "3":
        return_car()
    elif choice == "4":
        break
    else:
        print("Invalid choice!")
