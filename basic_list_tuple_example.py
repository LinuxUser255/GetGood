def basic_list_tuple_example():
    print("Basic Lists and Tuples Example\n")

    # List example
    print("List Example:")
    fruits = ["apple", "banana", "cherry"]
    print(f"Fruit list: {fruits}")

    # Accessing list elements
    print(f"First fruit: {fruits[0]}")
    print(f"Last fruit: {fruits[-1]}")

    # Modifying a list
    fruits.append("date")
    print(f"After adding 'date': {fruits}")

    fruits[1] = "blueberry"
    print(f"After changing 'banana' to 'blueberry': {fruits}")

    print("\n" + "-"*20 + "\n")

    # Tuple example
    print("Tuple Example:")
    colors = ("red", "green", "blue")
    print(f"Color tuple: {colors}")

    # Accessing tuple elements
    print(f"First color: {colors[0]}")
    print(f"Last color: {colors[-1]}")

    # Demonstrating tuple immutability
    try:
        colors[1] = "yellow"
    except TypeError as e:
        print(f"Error when trying to modify tuple: {e}")

def main():
    basic_list_tuple_example()

if __name__ == "__main__":
    main()