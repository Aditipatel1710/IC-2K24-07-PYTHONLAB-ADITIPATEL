# This program takes the user's name, age, height and student status as input
# and displays each value along with its data type.

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))

student_input = input("Are you a student? (True/False): ")
is_student = student_input == "True"

print("\n--- Details ---")
print("Name:", name, "Type:", type(name))
print("Age:", age, "Type:", type(age))
print("Height:", height, "Type:", type(height))
print("Student:", is_student, "Type:", type(is_student))