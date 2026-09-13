accounts = {}

def create_account():
    number = input("Enter Account Number: ")

    if number in accounts:
        print("Account already exists!")
        return

    name = input("Enter Account Holder Name: ")
    amount = float(input("Enter Initial Deposit: "))

    accounts[number] = {
        "name": name,
        "balance": amount
    }

    print("Account created successfully!")


def deposit():
    number = input("Enter Account Number: ")

    if number not in accounts:
        print("Account not found!")
        return

    amount = float(input("Enter amount: "))

    if amount > 0:
        accounts[number]["balance"] += amount
        print("Deposit successful!")
    else:
        print("Invalid amount!")


def withdraw():
    number = input("Enter Account Number: ")

    if number not in accounts:
        print("Account not found!")
        return

    amount = float(input("Enter amount: "))

    if amount <= 0:
        print("Invalid amount!")
    elif amount > accounts[number]["balance"]:
        print("Insufficient balance!")
    else:
        accounts[number]["balance"] -= amount
        print("Withdrawal successful!")


def check_balance():
    number = input("Enter Account Number: ")

    if number in accounts:
        print("Balance:", accounts[number]["balance"])
    else:
        print("Account not found!")


while True:
    print("\n===== BANK MANAGEMENT =====")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        check_balance()
    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
