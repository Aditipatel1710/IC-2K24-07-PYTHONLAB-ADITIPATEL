num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)

# Division and remainder are not possible when the second number is zero.
if num2 != 0:
    print("Quotient:", num1 / num2)
    print("Remainder:", num1 % num2)
else:
    print("Quotient: Cannot divide by zero")
    print("Remainder: Cannot divide by zero")