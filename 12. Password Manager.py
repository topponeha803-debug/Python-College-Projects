passwords = {}

def add_password():
    website = input("Enter Website: ")

    if website in passwords:
        print("Password already saved!")
        return

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    passwords[website] = {
        "username": username,
        "password": password
    }

    print("Password saved!")


def search_password():
    website = input("Enter Website: ")

    if website not in passwords:
        print("No password found!")
        return

    data = passwords[website]

    print("\n--- Account Details ---")
    print("Website:", website)
    print("Username:", data["username"])
    print("Password:", data["password"])


def delete_password():
    website = input("Enter Website: ")

    if website in passwords:
        del passwords[website]
        print("Password deleted!")
    else:
        print("Website not found!")


def show_websites():
    if not passwords:
        print("No saved accounts!")
        return

    print("\nSaved Websites:")

    for website in passwords:
        print("-", website)


while True:
    print("\n===== PASSWORD MANAGER =====")
    print("1. Add Password")
    print("2. Search Password")
    print("3. Delete Password")
    print("4. Show Websites")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_password()
    elif choice == "2":
        search_password()
    elif choice == "3":
        delete_password()
    elif choice == "4":
        show_websites()
    elif choice == "5":
        break
    else:
        print("Invalid choice!")
