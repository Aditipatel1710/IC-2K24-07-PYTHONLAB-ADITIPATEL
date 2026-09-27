# This program takes a full name as input
# and performs different string manipulations.
full_name = input("Enter your full name: ")
print("Uppercase:", full_name.upper())
print("Lowercase:", full_name.lower())
print("Reversed:", full_name[::-1])
print("Length:", len(full_name))
print("Without extra spaces:", full_name.strip())