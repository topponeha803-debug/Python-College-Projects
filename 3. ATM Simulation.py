balance = 10000
correct_pin = "1234"

def check_balance():
    print("Current Balance:", balance)


def deposit():
    global balance

    amount = float(input("Enter deposit amount: "))

    if amount > 0:
        balance += amount
        print("Amount deposited successfully!")
    else:
        print("Invalid amount!")


def withdraw():
    global balance

    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        print("Invalid amount!")
    elif amount > balance:
        print("Insufficient balance!")
    else:
        balance -= amount
        print("Please collect your cash.")
        print("Remaining Balance:", balance)


def atm():
    global balance

    pin = input("Enter your PIN: ")

    if pin != correct_pin:
        print("Incorrect PIN!")
        return

    print("\nLogin successful!")

    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            check_balance()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            print("Thank you!")
            break

        else:
            print("Invalid option!")


atm()
