# Combined Application
# ATM + Student Grade Calculator + Guessing Game

import random


# ================= ATM =================

balance = 5000
pin = "1234"


def atm():
    global balance, pin

    entered_pin = input("\nEnter ATM PIN: ")

    if entered_pin != pin:
        print("Incorrect PIN! Access denied.")
        return

    print("PIN verified successfully!")

    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change PIN")
        print("5. Exit ATM")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Current Balance: ₹", balance)

        elif choice == "2":
            amount = float(input("Enter deposit amount: ₹"))

            if amount > 0:
                balance += amount
                print("Amount deposited successfully.")
                print("Current Balance: ₹", balance)
            else:
                print("Invalid amount!")

        elif choice == "3":
            amount = float(input("Enter withdrawal amount: ₹"))

            if amount <= 0:
                print("Invalid amount!")

            elif amount > balance:
                print("Insufficient balance! Withdrawal rejected.")

            else:
                balance -= amount
                print("Amount withdrawn successfully.")
                print("Current Balance: ₹", balance)

        elif choice == "4":
            old_pin = input("Enter current PIN: ")

            if old_pin == pin:
                new_pin = input("Enter new 4-digit PIN: ")

                if len(new_pin) == 4 and new_pin.isdigit():
                    pin = new_pin
                    print("PIN changed successfully!")
                else:
                    print("PIN must contain exactly 4 digits.")
            else:
                print("Incorrect current PIN!")

        elif choice == "5":
            print("Exiting ATM...")
            break

        else:
            print("Invalid choice!")


# ================= GRADE CALCULATOR =================

last_student = None


def grade_calculator():
    global last_student

    while True:
        print("\n===== GRADE CALCULATOR =====")
        print("1. Enter marks for a new student")
        print("2. View grade of last entered student")
        print("3. Exit Grade Calculator")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            marks = []

            for i in range(1, 6):
                while True:
                    mark = float(input(f"Enter marks for Subject {i}: "))

                    if 0 <= mark <= 100:
                        marks.append(mark)
                        break
                    else:
                        print("Marks must be between 0 and 100.")

            average = sum(marks) / 5

            if average >= 90:
                grade = "A+"
            elif average >= 80:
                grade = "A"
            elif average >= 70:
                grade = "B"
            elif average >= 60:
                grade = "C"
            elif average >= 50:
                grade = "D"
            else:
                grade = "F"

            last_student = [name, marks, average, grade]

            print("Student data entered successfully!")

        elif choice == "2":
            if last_student is None:
                print("No student data available.")
            else:
                print("\n===== LAST STUDENT =====")
                print("Name:", last_student[0])
                print("Marks:", last_student[1])
                print("Average:", round(last_student[2], 2))
                print("Grade:", last_student[3])

        elif choice == "3":
            print("Exiting Grade Calculator...")
            break

        else:
            print("Invalid choice!")


# ================= GUESSING GAME =================

def guessing_game():

    secret_number = random.randint(1, 100)
    score = 100
    max_attempts = 7

    print("\n===== GUESSING GAME =====")
    print("Guess a number between 1 and 100.")
    print("You have 7 attempts.")

    for attempt in range(1, max_attempts + 1):

        guess = int(input(f"Attempt {attempt}: Enter your guess: "))

        if guess == secret_number:
            print("Congratulations! You guessed correctly!")
            print("Final Score:", score)
            break

        elif guess < secret_number:
            print("Too low!")

        else:
            print("Too high!")

        if secret_number % 2 == 0:
            print("Hint: Secret number is even.")
        else:
            print("Hint: Secret number is odd.")

        if secret_number % 5 == 0:
            print("Hint: Secret number is a multiple of 5.")
        else:
            print("Hint: Secret number is not a multiple of 5.")

        score -= 10
        print("Current Score:", score)

    else:
        print("\nYou lost!")
        print("The secret number was:", secret_number)
        print("Final Score: 0")


# ================= MAIN MENU =================

while True:

    print("\n================================")
    print("       COMBINED APPLICATION")
    print("================================")
    print("1. ATM")
    print("2. Grade Calculator")
    print("3. Guessing Game")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        atm()

    elif choice == "2":
        grade_calculator()

    elif choice == "3":
        guessing_game()

    elif choice == "4":
        print("Thank you for using the application!")
        break

    else:
        print("Invalid choice! Please select 1-4.")