# This program checks whether a number is a perfect number
# and prints all perfect numbers up to a user-defined limit.


def is_perfect(number):
    if number <= 0:
        return False

    divisors_sum = 0

    # Proper divisors are numbers that divide the number
    # without including the number itself.
    for i in range(1, number):
        if number % i == 0:
            divisors_sum += i

    return divisors_sum == number


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


# Check one number
number = get_positive_integer("Enter a positive number: ")

if is_perfect(number):
    print(number, "is a perfect number.")
else:
    print(number, "is not a perfect number.")


# Print all perfect numbers up to the given limit
print("\n--- Perfect Numbers up to a Limit ---")

limit = get_positive_integer("Enter the limit: ")

perfect_numbers = []

for number in range(1, limit + 1):
    if is_perfect(number):
        perfect_numbers.append(number)

print("Perfect numbers:", perfect_numbers)