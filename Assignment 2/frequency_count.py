paragraph = input("Enter a paragraph: ")

# Convert to lowercase
paragraph = paragraph.lower()

# Remove punctuation manually without using a library
cleaned = ""

for char in paragraph:
    if char.isalnum() or char.isspace():
        cleaned += char
    else:
        cleaned += " "

# Split paragraph into words
words = cleaned.split()

if not words:
    print("No words found in the paragraph.")

else:
    # Count word frequency using get()
    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    print("\nWord Frequencies:")
    print(frequency)

    # Top N words, ties broken alphabetically
    n = int(input("\nEnter N: "))

    sorted_words = sorted(
        frequency.items(),
        key=lambda x: (-x[1], x[0])
    )

    print("\nTop", n, "Words:")
    for word, count in sorted_words[:max(0, n)]:
        print(word, "=", count)

    # Words appearing exactly once
    once = [
        word for word, count in frequency.items()
        if count == 1
    ]

    print("\nWords appearing once:")
    print(sorted(once))

    # Invert dictionary: frequency -> words
    inverted = {}

    for word, count in frequency.items():
        inverted.setdefault(count, []).append(word)

    # Sort each list alphabetically
    for count in inverted:
        inverted[count].sort()

    print("\nInverted Dictionary:")
    print(inverted)

    # Group words by length
    length_groups = {}

    for word in frequency:
        length = len(word)
        length_groups.setdefault(length, []).append(word)

    for length in length_groups:
        length_groups[length].sort()

    print("\nWords Grouped by Length:")
    print(length_groups)

    # Search for a word
    search_word = input("\nEnter word to search: ").lower()

    print(
        "Count:",
        frequency.get(search_word, "Word not found")
    )