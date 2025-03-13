#!/usr/bin/env python3

def generate_values():
    """list comprehension examples"""

    values_traditional = [] # traditional way to generate values
    for x in range(11):
        values_traditional.append(x)
    print("Values generated traditionally:", values_traditional)

    values_comprehension = [x for x in range(11)] # Using list comprehension
    print("Values generated using list comprehension:", values_comprehension)

def main():
    generate_values()
    print("main function called.")

if __name__ == "__main__":
    main()