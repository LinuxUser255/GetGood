#!/usr/bin/env python3


def list_comprehension_example():
    print("List Comprehension Examples\n")

    # Example 1: Squaring numbers
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = [x**2 for x in numbers]
    print("1. Squaring numbers:")
    print(f"   Original numbers: {numbers}")
    print(f"   Squared numbers: {squared_numbers}\n")

    # Example 2: Filtering even numbers
    numbers = range(1, 11)
    even_numbers = [x for x in numbers if x % 2 == 0]
    print("2. Filtering even numbers:")
    print(f"   Numbers from 1 to 10: {list(numbers)}")
    print(f"   Even numbers: {even_numbers}\n")

    # Example 3: Creating a list of tuples (number, square)
    number_squares = [(x, x**2) for x in range(1, 6)]
    print("3. Creating (number, square) tuples:")
    print(f"   Result: {number_squares}\n")

    # Example 4: Flattening a 2D list
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened = [num for row in matrix for num in row]
    print("4. Flattening a 2D list:")
    print(f"   Original matrix: {matrix}")
    print(f"   Flattened list: {flattened}\n")

    # Example 5: Creating a list of uppercase letters from a string
    text = "hello world"
    uppercase_letters = [char.upper() for char in text if char.isalpha()]
    print("5. Uppercase letters from a string:")
    print(f"   Original text: '{text}'")
    print(f"   Uppercase letters: {uppercase_letters}\n")

def main():
    list_comprehension_example()

if __name__ == "__main__":
    main()