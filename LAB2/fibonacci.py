# This program generates the Fibonacci series using a loop
# and recursion, and compares the number of recursive calls.


def fibonacci_loop(n):
    series = []

    first = 0
    second = 1

    for i in range(n):
        series.append(first)

        # Update the two Fibonacci values for the next iteration.
        first, second = second, first + second

    return series


recursive_calls = 0


def fibonacci_recursive(n):
    global recursive_calls

    recursive_calls += 1

    if n <= 1:
        return n

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


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


n = get_positive_integer("Enter the number of terms: ")


# Fibonacci using loop
loop_series = fibonacci_loop(n)
print("\nFibonacci using loop:")
print(loop_series)


# Fibonacci using recursion
recursive_series = []

for i in range(n):
    recursive_series.append(fibonacci_recursive(i))

print("\nFibonacci using recursion:")
print(recursive_series)

print("\nNumber of recursive function calls:", recursive_calls)