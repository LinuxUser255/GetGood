def dictionary_example():
    print("Dictionary Example\n")

    # Creating a dictionary
    student = {
        "name": "Alice",
        "age": 20,
        "major": "Computer Science",
        "gpa": 3.8
    }

    # Accessing dictionary values
    print(f"Student Name: {student['name']}")
    print(f"Student Age: {student['age']}")

    # Adding a new key-value pair
    student["year"] = "Sophomore"
    print(f"\nAfter adding year: {student}")

    # Modifying an existing value
    student["age"] = 21
    print(f"After updating age: {student}")

    # Removing a key-value pair
    removed_major = student.pop("major")
    print(f"\nRemoved major: {removed_major}")
    print(f"After removing major: {student}")

    # Checking if a key exists
    if "gpa" in student:
        print(f"\nThe student's GPA is: {student['gpa']}")

    # Getting all keys and values
    print("\nAll keys:", list(student.keys()))
    print("All values:", list(student.values()))

    # Iterating through the dictionary
    print("\nIterating through the dictionary:")
    for key, value in student.items():
        print(f"{key}: {value}")

    # Using get() method with a default value
    print(f"\nStudent's grade: {student.get('grade', 'Not Available')}")

def main():
    dictionary_example()

if __name__ == "__main__":
    main()