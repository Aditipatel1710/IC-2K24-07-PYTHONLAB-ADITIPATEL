# ATM Simulation - Menu Driven Program

balance = 5000
pin = "1234"


def check_balance():
    print(f"Current Balance: ₹{balance}")


def deposit():
    global balance

    amount = float(input("Enter amount to deposit: ₹"))

    if amount <= 0:
        print("Invalid amount! Deposit must be greater than 0.")
    else:
        balance += amount
        print(f"₹{amount} deposited successfully.")
        print(f"Updated Balance: ₹{balance}")


def withdraw():
    global balance

    amount = float(input("Enter amount to withdraw: ₹"))

    if amount <= 0:
        print("Invalid amount! Withdrawal must be greater than 0.")
    elif amount > balance:
        print("Insufficient balance! Withdrawal rejected.")
    else:
        balance -= amount
        print(f"₹{amount} withdrawn successfully.")
        print(f"Remaining Balance: ₹{balance}")


def change_pin():
    global pin

    old_pin = input("Enter your current PIN: ")

    if old_pin != pin:
        print("Incorrect current PIN!")
        return

    new_pin = input("Enter new PIN: ")

    if len(new_pin) != 4 or not new_pin.isdigit():
        print("PIN must contain exactly 4 digits.")
    else:
        pin = new_pin
        print("PIN changed successfully!")


# PIN verification
print("===== ATM SIMULATION =====")

entered_pin = input("Enter your PIN: ")

if entered_pin != pin:
    print("Incorrect PIN! Access denied.")
else:
    print("PIN verified successfully!")

    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change PIN")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            change_pin()

        elif choice == "5":
            print("Thank you for using the ATM!")
            break

        else:
            print("Invalid choice! Please select 1-5.")