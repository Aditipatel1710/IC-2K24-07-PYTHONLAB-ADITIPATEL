# This program combines Armstrong, Prime, Perfect Number,
# Palindrome, Fibonacci and Pattern programs into one menu.


def get_non_negative_integer(message):
    while True:
        try:
            number = int(input(message))

            if number >= 0:
                return number
            else:
                print("Please enter a non-negative integer.")

        except ValueError:
            print("Invalid input! Please enter an integer.")


def get_positive_integer(message):
    while True:
        try:
            number = int(input(message))

            if number > 0:
                return number
            else:
                print("Please enter a positive integer.")

        except ValueError:
            print("Invalid input! Please enter an integer.")


# ---------- Armstrong ----------

def is_armstrong(number):
    digits = len(str(number))
    total = 0
    temp = number

    if number == 0:
        return True

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    return total == number


def armstrong_option():
    number = get_non_negative_integer("Enter a number: ")

    if is_armstrong(number):
        print("It is an Armstrong number.")
    else:
        print("It is not an Armstrong number.")

    start = get_non_negative_integer("Enter range start: ")
    end = get_non_negative_integer("Enter range end: ")

    if start > end:
        print("Invalid range.")
        return

    result = []

    for i in range(start, end + 1):
        if is_armstrong(i):
            result.append(i)

    print("Armstrong numbers:", result)


# ---------- Prime ----------

def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


def prime_option():
    number = get_non_negative_integer("Enter a number: ")

    if is_prime(number):
        print("It is a prime number.")
    else:
        print("It is not a prime number.")

    limit = get_non_negative_integer("Enter limit: ")

    primes = []

    for i in range(2, limit + 1):
        if is_prime(i):
            primes.append(i)

    print("Prime numbers:", primes)


# ---------- Perfect Number ----------

def is_perfect(number):
    if number <= 0:
        return False

    total = 0

    for i in range(1, number):
        if number % i == 0:
            total += i

    return total == number


def perfect_option():
    number = get_positive_integer("Enter a positive number: ")

    if is_perfect(number):
        print("It is a perfect number.")
    else:
        print("It is not a perfect number.")

    limit = get_positive_integer("Enter limit: ")

    perfect_numbers = []

    for i in range(1, limit + 1):
        if is_perfect(i):
            perfect_numbers.append(i)

    print("Perfect numbers:", perfect_numbers)


# ---------- Palindrome ----------

def is_number_palindrome(number):
    original = number
    reversed_number = 0

    while number > 0:
        digit = number % 10

        # Construct the reverse using arithmetic only.
        reversed_number = reversed_number * 10 + digit
        number //= 10

    return original == reversed_number


def palindrome_option():
    number = get_non_negative_integer("Enter a number: ")

    if is_number_palindrome(number):
        print("The number is a palindrome.")
    else:
        print("The number is not a palindrome.")

    text = input("Enter a string: ")
    text = text.lower()

    if text == text[::-1]:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")


# ---------- Fibonacci ----------

def fibonacci_option():
    n = get_positive_integer("Enter number of terms: ")

    first = 0
    second = 1
    series = []

    for i in range(n):
        series.append(first)

        # Update both values for the next Fibonacci term.
        first, second = second, first + second

    print("Fibonacci series:", series)


# ---------- Patterns ----------

def patterns_option():
    n = get_positive_integer("Enter number of rows: ")

    print("\nRight-Angled Triangle")

    for i in range(1, n + 1):
        for j in range(i):
            print("*", end=" ")
        print()

    print("\nNumber Pattern")

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

    print("\nCentered Pyramid")

    for i in range(1, n + 1):

        # Spaces center the pyramid.
        for j in range(n - i):
            print(" ", end=" ")

        for j in range(2 * i - 1):
            print("*", end=" ")

        print()


# ---------- Main Menu ----------

while True:
    print("\n========== MENU ==========")
    print("1. Armstrong Number")
    print("2. Prime Number")
    print("3. Perfect Number")
    print("4. Palindrome")
    print("5. Fibonacci Series")
    print("6. Pattern Printing")
    print("7. Exit")
    print("==========================")

    choice = input("Enter your choice: ")

    if choice == "1":
        armstrong_option()

    elif choice == "2":
        prime_option()

    elif choice == "3":
        perfect_option()

    elif choice == "4":
        palindrome_option()

    elif choice == "5":
        fibonacci_option()

    elif choice == "6":
        patterns_option()

    elif choice == "7":
        print("Program exited successfully.")
        break

    else:
        print("Invalid choice! Please select 1 to 7.")