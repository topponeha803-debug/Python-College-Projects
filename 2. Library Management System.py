books = {
    "101": {"name": "Python Basics", "issued": False},
    "102": {"name": "Computer Fundamentals", "issued": False},
    "103": {"name": "Operating Systems", "issued": False}
}

def show_books():
    print("\n--- Available Books ---")

    for code, book in books.items():
        status = "Issued" if book["issued"] else "Available"
        print(code, "-", book["name"], "-", status)


def add_book():
    code = input("Enter Book ID: ")

    if code in books:
        print("Book already exists!")
        return

    name = input("Enter Book Name: ")

    books[code] = {
        "name": name,
        "issued": False
    }

    print("Book added successfully!")


def issue_book():
    code = input("Enter Book ID: ")

    if code not in books:
        print("Book not found!")
        return

    if books[code]["issued"]:
        print("Book is already issued!")
    else:
        books[code]["issued"] = True
        print("Book issued successfully!")


def return_book():
    code = input("Enter Book ID: ")

    if code not in books:
        print("Book not found!")
        return

    if not books[code]["issued"]:
        print("Book was not issued.")
    else:
        books[code]["issued"] = False
        print("Book returned successfully!")


def search_book():
    name = input("Enter book name: ").lower()

    found = False

    for code, book in books.items():
        if name in book["name"].lower():
            print(code, book["name"])
            found = True

    if not found:
        print("Book not found!")


while True:
    print("\n===== LIBRARY SYSTEM =====")
    print("1. Show Books")
    print("2. Add Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Search Book")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        show_books()
    elif choice == "2":
        add_book()
    elif choice == "3":
        issue_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        search_book()
    elif choice == "6":
        break
    else:
        print("Invalid choice!")
