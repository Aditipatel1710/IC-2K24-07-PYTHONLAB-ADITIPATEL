books = {
    "B1": {
        "title": "Python Basics",
        "author": "Rao",
        "copies": 2,
        "issued_to": []
    },
    "B2": {
        "title": "Data Structures",
        "author": "Iyer",
        "copies": 1,
        "issued_to": []
    },
    "B3": {
        "title": "Algorithms",
        "author": "Rao",
        "copies": 1,
        "issued_to": []
    }
}


def reports():
    # Books by a given author
    author = input("Enter author name: ")

    result = [
        b["title"] for b in books.values()
        if b["author"].lower() == author.lower()
    ]

    print("Books by author:", result)

    # Invert book data into member -> books
    members = {}

    for isbn, book in books.items():
        for member in book["issued_to"]:
            members.setdefault(member, []).append(book["title"])

    print("\nMembers holding more than one book:")
    for member, titles in members.items():
        if len(titles) > 1:
            print(member, "->", titles)

    # Unavailable books
    unavailable = [
        b["title"] for b in books.values()
        if b["copies"] == 0
    ]

    print("\nUnavailable Books:", unavailable)

    # Books never issued
    never_issued = [
        b["title"] for b in books.values()
        if not b["issued_to"]
    ]

    print("Never Issued Books:", never_issued)


while True:
    print("\n--- LIBRARY SYSTEM ---")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Search Book")
    print("5. Reports")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        isbn = input("ISBN: ")

        if isbn in books:
            copies = int(input("Additional copies: "))
            if copies > 0:
                books[isbn]["copies"] += copies
                print("Copies added.")
            else:
                print("Copies must be positive.")
        else:
            title = input("Title: ")
            author = input("Author: ")
            copies = int(input("Copies: "))

            if copies > 0:
                books[isbn] = {
                    "title": title,
                    "author": author,
                    "copies": copies,
                    "issued_to": []
                }
                print("Book added.")
            else:
                print("Invalid number of copies.")

    elif choice == "2":
        isbn = input("ISBN: ")
        member = input("Member ID: ")

        if isbn not in books:
            print("Book not found.")
            continue

        book = books[isbn]

        if member in book["issued_to"]:
            print("Member already holds this book.")

        elif book["copies"] <= 0:
            print("No copies available.")

        else:
            total_held = sum(
                member in b["issued_to"] for b in books.values()
            )

            if total_held >= 2:
                print("Member has reached the 2-book limit.")
            else:
                book["copies"] -= 1
                book["issued_to"].append(member)
                print("Book issued successfully.")

    elif choice == "3":
        isbn = input("ISBN: ")
        member = input("Member ID: ")

        if isbn not in books:
            print("Book not found.")
        elif member not in books[isbn]["issued_to"]:
            print("Member does not hold this book.")
        else:
            books[isbn]["issued_to"].remove(member)
            books[isbn]["copies"] += 1
            print("Book returned successfully.")

    elif choice == "4":
        isbn = input("Enter ISBN: ")
        print(books.get(isbn, "Book not found."))

    elif choice == "5":
        reports()

    elif choice == "6":
        print("Exiting Library System.")
        break

    else:
        print("Invalid choice!")