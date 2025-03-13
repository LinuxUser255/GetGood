from typing import List, Tuple, Dict, Set

# This function is called in the main function
def basic_data_types_example() -> None:
    print("Basic Python Data Types Example\n")

    # Integer
    age: int = 30
    print(f"1. Integer (int):")
    print(f"   Age: {age}")
    print(f"   Type: {type(age)}")
    print()

    # Float
    height: float = 5.9
    print(f"2. Float:")
    print(f"   Height: {height}")
    print(f"   Type: {type(height)}")
    print()

    # String
    name: str = "Alice"
    print(f"3. String (str):")
    print(f"   Name: {name}")
    print(f"   Type: {type(name)}")
    print()

    # Boolean
    is_student: bool = True
    print(f"4. Boolean (bool):")
    print(f"   Is student: {is_student}")
    print(f"   Type: {type(is_student)}")
    print()

    # List
    fruits: List[str] = ["apple", "banana", "cherry"]
    print(f"5. List:")
    print(f"   Fruits: {fruits}")
    print(f"   Type: {type(fruits)}")
    print(f"   First fruit: {fruits[0]}")
    print()

    # Tuple
    coordinates: Tuple[int, int] = (10, 20)
    print(f"6. Tuple:")
    print(f"   Coordinates: {coordinates}")
    print(f"   Type: {type(coordinates)}")
    print(f"   X-coordinate: {coordinates[0]}")
    print()

    # Dictionary
    person: Dict[str, Union[str, int]] = {"name": "Bob", "age": 25, "city": "New York"}
    print(f"7. Dictionary (dict):")
    print(f"   Person: {person}")
    print(f"   Type: {type(person)}")
    print(f"   Name: {person['name']}")
    print()

    # Set
    unique_numbers: Set[int] = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
    print(f"8. Set:")
    print(f"   Unique numbers: {unique_numbers}")
    print(f"   Type: {type(unique_numbers)}")
    print()

def main() -> None:
    basic_data_types_example()

if __name__ == "__main__":
    main()