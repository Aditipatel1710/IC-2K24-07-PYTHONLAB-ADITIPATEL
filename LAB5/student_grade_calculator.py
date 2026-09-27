# Student Grade Calculator - Menu Driven Program

last_student = None


def enter_student():
    global last_student

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

    # Grade scheme
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

    print("\nStudent data entered successfully!")


def view_grade():
    if last_student is None:
        print("No student data has been entered yet.")
    else:
        print("\n===== LAST ENTERED STUDENT =====")
        print("Name:", last_student[0])
        print("Marks:", last_student[1])
        print("Average:", round(last_student[2], 2))
        print("Grade:", last_student[3])


while True:
    print("\n===== STUDENT GRADE CALCULATOR =====")
    print("1. Enter marks for a new student")
    print("2. View grade of last entered student")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        enter_student()

    elif choice == "2":
        view_grade()

    elif choice == "3":
        print("Exiting Grade Calculator...")
        break

    else:
        print("Invalid choice! Please enter 1-3.")