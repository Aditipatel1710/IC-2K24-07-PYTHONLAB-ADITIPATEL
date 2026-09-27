# This program checks whether a number is prime
# and prints all prime numbers up to a user-defined limit.


def is_prime(number):
    if number < 2:
        return False

    # We only need to check divisors up to the square root of the number.
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


def get_positive_integer(message):
    while True:
        try:
            number = int(input(message))

            if number >= 0:
                return number
            else:
                print("Please enter a non-negative number.")

        except ValueError:
            print("Invalid input! Please enter an integer.")


# Check one number
number = get_positive_integer("Enter a number: ")

if is_prime(number):
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")


# Print all prime numbers up to a limit
print("\n--- Prime Numbers up to a Limit ---")

limit = get_positive_integer("Enter the limit: ")

prime_numbers = []

for number in range(2, limit + 1):
    if is_prime(number):
        prime_numbers.append(number)

print("Prime numbers:", prime_numbers)