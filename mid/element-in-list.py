#!/usr/bin/env python3

# Write a Python program to find the largest element in a list.
def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
            return largest

        # Test the program with a list of numbers
numbers = [2, 5, 9, 1, 7]
largest_num = find_largest(numbers)
print(f"The largest number in the list is: {largest_num}")

find_largest(numbers)