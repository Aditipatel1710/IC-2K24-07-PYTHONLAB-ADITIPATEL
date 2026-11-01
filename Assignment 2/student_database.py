students = {
    101: {"name": "Asha", "marks": {"Math": 88, "Physics": 76, "Chem": 92}},
    102: {"name": "Ravi", "marks": {"Math": 35, "Physics": 58, "Chem": 64}},
    103: {"name": "Meena", "marks": {"Math": 72, "Physics": 81, "Chem": 69}}
}

def reports():
    if not students:
        print("No student records available.")
        return

    # Average marks of every student
    averages = {
        roll: round(sum(s["marks"].values()) / len(s["marks"]), 2)
        for roll, s in students.items() if s["marks"]
    }
    print("\nStudent Averages:", averages)

    # Find topper
    if averages:
        topper = max(averages, key=averages.get)
        print("Topper:", students[topper]["name"])

    # Highest scorer in each subject
    subjects = {}
    for roll, s in students.items():
        for subject, marks in s["marks"].items():
            if subject not in subjects or marks > subjects[subject][1]:
                subjects[subject] = (s["name"], marks)

    print("\nHighest Scorer in Each Subject:")
    for subject, result in subjects.items():
        print(subject, "->", result[0], result[1])

    # Students scoring below 40
    print("\nBelow 40 in any subject:")
    for s in students.values():
        failed = [(sub, m) for sub, m in s["marks"].items() if m < 40]
        if failed:
            print(s["name"], failed)

    # Grade-wise grouping using average marks
    grades = {"A": [], "B": [], "C": [], "D": [], "F": []}

    for roll, avg in averages.items():
        name = students[roll]["name"]

        if avg >= 90:
            grades["A"].append(name)
        elif avg >= 75:
            grades["B"].append(name)
        elif avg >= 60:
            grades["C"].append(name)
        elif avg >= 40:
            grades["D"].append(name)
        else:
            grades["F"].append(name)

    print("\nGrade-wise Grouping:", grades)


while True:
    print("\n--- STUDENT DATABASE ---")
    print("1. Add Student")
    print("2. Update Marks")
    print("3. Delete Student")
    print("4. Show Student")
    print("5. Reports")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        roll = int(input("Enter roll number: "))

        if roll in students:
            print("Duplicate roll number!")
            continue

        name = input("Enter name: ")
        marks = {}

        n = int(input("Number of subjects: "))

        for i in range(n):
            sub = input("Subject: ")
            score = int(input("Marks: "))

            if not 0 <= score <= 100:
                print("Marks must be between 0 and 100.")
                break

            marks[sub] = score
        else:
            students[roll] = {"name": name, "marks": marks}
            print("Student added successfully.")

    elif choice == "2":
        roll = int(input("Enter roll number: "))

        if roll not in students:
            print("Student not found.")
            continue

        sub = input("Enter subject: ")
        score = int(input("Enter new marks: "))

        if 0 <= score <= 100:
            students[roll]["marks"][sub] = score
            print("Marks updated successfully.")
        else:
            print("Invalid marks!")

    elif choice == "3":
        roll = int(input("Enter roll number: "))

        if roll in students:
            del students[roll]
            print("Student deleted.")
        else:
            print("Student not found.")

    elif choice == "4":
        roll = int(input("Enter roll number: "))
        print(students.get(roll, "Student not found."))

    elif choice == "5":
        reports()

    elif choice == "6":
        print("Exiting Student Database.")
        break

    else:
        print("Invalid choice!")