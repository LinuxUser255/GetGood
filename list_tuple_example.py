def list_and_tuple_example():
    print("Lists and Tuples Example\n")

    # List example
    print("List Example:")
    fruits = ["apple", "banana", "cherry", "date"]
    print(f"Original fruit list: {fruits}")

    # Modifying a list
    fruits.append("elderberry")
    print(f"After adding elderberry: {fruits}")

    fruits[1] = "blueberry"
    print(f"After changing banana to blueberry: {fruits}")

    fruits.remove("cherry")
    print(f"After removing cherry: {fruits}")

    print(f"The second fruit in the list is: {fruits[1]}")

    print("\n" + "-"*20 + "\n")

    # Tuple example
    print("Tuple Example:")
    colors = ("red", "green", "blue", "yellow")
    print(f"Color tuple: {colors}")

    # Accessing tuple elements
    print(f"The first color is: {colors[0]}")
    print(f"The last color is: {colors[-1]}")

    # Attempting to modify a tuple (this will raise an error)
    try:
        colors[1] = "purple"
    except TypeError as e:
        print(f"Error when trying to modify tuple: {e}")

    # Unpacking a tuple
    first, second, third, fourth = colors
    print(f"Unpacked colors: {first}, {second}, {third}, {fourth}")

def main():
    list_and_tuple_example()

if __name__ == "__main__":
    main()