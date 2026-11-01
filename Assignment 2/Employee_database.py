employees = {
    "E1": {"name": "Kiran", "dept": "IT", "salary": 60000},
    "E2": {"name": "Sara", "dept": "HR", "salary": 45000},
    "E3": {"name": "Dev", "dept": "IT", "salary": 75000},
    "E4": {"name": "Nina", "dept": "Finance", "salary": 52000},
    "E5": {"name": "Omar", "dept": "HR", "salary": 48000}
}


def reports():
    if not employees:
        print("No employee records.")
        return

    payroll = {}
    headcount = {}
    highest = {}

    # Department-wise payroll and headcount in one pass
    for emp in employees.values():
        dept = emp["dept"]

        payroll[dept] = payroll.get(dept, 0) + emp["salary"]
        headcount[dept] = headcount.get(dept, 0) + 1

        if dept not in highest or emp["salary"] > highest[dept]["salary"]:
            highest[dept] = emp

    print("\nDepartment-wise Payroll:")
    print(payroll)

    print("Department-wise Headcount:")
    print(headcount)

    print("\nHighest Paid in Each Department:")
    for dept, emp in highest.items():
        print(dept, "->", emp["name"])

    # Sort employees by salary, highest first
    sorted_employees = sorted(
        employees.items(),
        key=lambda x: x[1]["salary"],
        reverse=True
    )

    print("\nEmployees Sorted by Salary:")
    for emp_id, emp in sorted_employees:
        print(emp_id, emp["name"], emp["salary"])

    # Create a new dictionary without changing original data.
    # A comprehension creates independent employee records, so the
    # original salary values remain unchanged.
    raised_employees = {
        emp_id: {
            **emp,
            "salary": emp["salary"] * 1.10
            if emp["salary"] < 50000 else emp["salary"]
        }
        for emp_id, emp in employees.items()
    }

    print("\nAfter 10% Raise:")
    for emp in raised_employees.values():
        print(emp["name"], emp["salary"])

    # Department with highest average salary
    averages = {
        dept: payroll[dept] / headcount[dept]
        for dept in payroll
    }

    best_dept = max(averages, key=averages.get)

    print("\nDepartment with Highest Average Salary:")
    print(best_dept, averages[best_dept])


while True:
    print("\n--- EMPLOYEE DATABASE ---")
    print("1. Add Employee")
    print("2. Update Salary")
    print("3. Delete Employee")
    print("4. Search by ID")
    print("5. Reports")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        emp_id = input("Employee ID: ")

        if emp_id in employees:
            print("Employee already exists.")
            continue

        name = input("Name: ")
        dept = input("Department: ")
        salary = float(input("Salary: "))

        employees[emp_id] = {
            "name": name,
            "dept": dept,
            "salary": salary
        }

        print("Employee added.")

    elif choice == "2":
        emp_id = input("Employee ID: ")

        if emp_id in employees:
            salary = float(input("New salary: "))
            employees[emp_id]["salary"] = salary
            print("Salary updated.")
        else:
            print("Employee not found.")

    elif choice == "3":
        emp_id = input("Employee ID: ")

        if emp_id in employees:
            del employees[emp_id]
            print("Employee deleted.")
        else:
            print("Employee not found.")

    elif choice == "4":
        emp_id = input("Employee ID: ")
        print(employees.get(emp_id, "Employee not found"))

    elif choice == "5":
        reports()

    elif choice == "6":
        print("Exiting.")
        break

    else:
        print("Invalid choice!")