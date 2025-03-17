#!/usr/bin/env python3

def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

def basic_control_flow_example():
    print("Basic Control Flow Example\n")

    # If-elif-else example
    print("1. If-elif-else example:")
    number = int(input("Enter a number: "))
    result = check_number(number)
    print(f"The number {number} is {result}")

    print("\n" + "-"*20 + "\n")

    # For loop example
    print("2. For loop example:")
    print("Counting from 1 to 5:")
    for i in range(1, 6):
        print(i, end=" ")
    print("\n")

    print("\n" + "-"*20 + "\n")

    # While loop example
    print("3. While loop example:")
    print("Counting down from 5 to 1:")
    count = 5
    while count > 0:
        print(count, end=" ")
        count -= 1
    print("\n")

    print("\n" + "-"*20 + "\n")

    # Break and continue example
    print("4. Break and continue example:")
    print("Printing odd numbers from 1 to 10 (skipping 5):")
    for i in range(1, 11):
        if i % 2 == 0:
            continue
        if i == 5:
            continue
        if i > 7:
            break
        print(i, end=" ")
    print("\n")

def run_it():
    basic_control_flow_example()

#if __name__ == "__main__":
    #main()