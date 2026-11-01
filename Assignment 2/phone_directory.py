contacts = {
    "Anita": {
        "phones": ["9876543210"],
        "email": "anita@mail.com",
        "city": "Pune"
    },

    "Manoj": {
        "phones": ["9123456780", "9988776655"],
        "email": "manoj@mail.com",
        "city": "Delhi"
    },

    "Zara": {
        "phones": ["9000011111"],
        "email": "zara@mail.com",
        "city": "Pune"
    }
}


# Validate phone number
def valid_phone(number):
    return len(number) == 10 and number.isdigit()


# Check whether number belongs to another contact
def number_owner(number):
    for name, data in contacts.items():
        if number in data["phones"]:
            return name
    return None


while True:
    print("\n--- PHONE DIRECTORY ---")
    print("1. Add Contact")
    print("2. Add Another Number")
    print("3. Update Email or City")
    print("4. Delete Contact")
    print("5. Search")
    print("6. Reports")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")

        if name in contacts:
            print("Contact already exists.")
            continue

        number = input("Enter phone number: ")

        if not valid_phone(number):
            print("Phone number must contain exactly 10 digits.")
            continue

        owner = number_owner(number)

        if owner:
            print("Number already belongs to", owner)
            continue

        email = input("Enter email: ")
        city = input("Enter city: ")

        contacts[name] = {
            "phones": [number],
            "email": email,
            "city": city
        }

        print("Contact added successfully.")

    elif choice == "2":
        name = input("Enter contact name: ")

        if name not in contacts:
            print("Contact not found.")
            continue

        number = input("Enter another number: ")

        if not valid_phone(number):
            print("Invalid number. Must be 10 digits.")

        elif number_owner(number):
            print("Number already belongs to", number_owner(number))

        else:
            contacts[name]["phones"].append(number)
            print("Number added successfully.")

    elif choice == "3":
        name = input("Enter contact name: ")

        if name not in contacts:
            print("Contact not found.")
            continue

        print("1. Update Email")
        print("2. Update City")

        option = input("Enter option: ")

        if option == "1":
            contacts[name]["email"] = input("New email: ")
            print("Email updated.")

        elif option == "2":
            contacts[name]["city"] = input("New city: ")
            print("City updated.")

        else:
            print("Invalid option.")

    elif choice == "4":
        name = input("Enter name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    elif choice == "5":
        print("1. Search by partial name")
        print("2. Reverse lookup by phone number")

        option = input("Enter option: ")

        if option == "1":
            search = input("Enter name: ").lower()

            found = False

            for name, data in contacts.items():
                if search in name.lower():
                    print(name, "->", data)
                    found = True

            if not found:
                print("Contact not found.")

        elif option == "2":
            number = input("Enter phone number: ")

            # Reverse lookup using dictionary comprehension
            reverse = {
                phone: name
                for name, data in contacts.items()
                for phone in data["phones"]
            }

            print(reverse.get(number, "Number not found."))

    elif choice == "6":
        if not contacts:
            print("Directory is empty.")
            continue

        # Group contacts by city
        city_groups = {}

        for name, data in contacts.items():
            city = data["city"]
            city_groups.setdefault(city, []).append(name)

        print("\nContacts Grouped by City:")
        print(city_groups)

        # Contacts having more than one number
        multiple = [
            name for name, data in contacts.items()
            if len(data["phones"]) > 1
        ]

        print("\nContacts with Multiple Numbers:")
        print(multiple)

        # Print entire directory alphabetically
        print("\nComplete Phone Directory:")

        for name in sorted(contacts):
            print("\nName:", name)
            print("Phones:", contacts[name]["phones"])
            print("Email:", contacts[name]["email"])
            print("City:", contacts[name]["city"])

    elif choice == "7":
        print("Exiting Phone Directory.")
        break

    else:
        print("Invalid choice!")