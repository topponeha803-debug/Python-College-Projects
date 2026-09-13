movies = {
    1: {"name": "Avengers", "price": 250, "seats": 50},
    2: {"name": "Dangal", "price": 200, "seats": 40},
    3: {"name": "3 Idiots", "price": 180, "seats": 30},
    4: {"name": "Pathaan", "price": 220, "seats": 35}
}

def show_movies():
    print("\n===== MOVIES =====")

    for number, movie in movies.items():
        print(
            number,
            movie["name"],
            "- ₹",
            movie["price"],
            "- Seats:",
            movie["seats"]
        )


def book_ticket():
    show_movies()

    choice = int(input("Select movie: "))

    if choice not in movies:
        print("Invalid movie!")
        return

    movie = movies[choice]

    seats = int(input("Enter number of tickets: "))

    if seats <= 0:
        print("Invalid number!")
        return

    if seats > movie["seats"]:
        print("Not enough seats!")
        return

    name = input("Enter customer name: ")

    amount = seats * movie["price"]

    movie["seats"] -= seats

    print("\n===== BOOKING CONFIRMED =====")
    print("Customer:", name)
    print("Movie:", movie["name"])
    print("Tickets:", seats)
    print("Amount: ₹", amount)
    print("Remaining Seats:", movie["seats"])


while True:
    print("\n===== MOVIE TICKET SYSTEM =====")
    print("1. Show Movies")
    print("2. Book Ticket")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        show_movies()
    elif choice == "2":
        book_ticket()
    elif choice == "3":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
