#!/usr/bin/env python3

from advanced.iter_range import MyRange
from manage_file_context import FileManager
from generate import count_up_to


def decorator_example(func):
    def wrapper(*args, **kwargs):
        print(f'Decorator func: Before the function execution')
        result = func(*args, **kwargs)
        print(f'Decorator func: After the function execution')
        return result

    return wrapper


@decorator_example
def say_hello(name):
    # same as: say_hello = decorator_example(say_hello)
    # say_hello("Alice")
    print(f'Hello, {name}!')


@decorator_example
def calculate_square(number):
    return number ** 2


# Create a function that uses code from manage_file_context.py
def write_to_file(filename, content):
    with FileManager(filename, "w") as file:
        file.write(content)
        print(f'File {filename} written successfully.')
        return True


def iterate_range(start, end):
    # importing MyRange from advanced.iter_range.py
    my_range = MyRange(start, end)
    for number in my_range:
        print(number)


def generate_yields(limit):
    # importing count_up_to from generate.py
    for number in count_up_to(limit):
        yield number


def main():
    say_hello("Alice")
    result = calculate_square(5)
    print(f'The square of 5 is: {result}')
    write_to_file("example.txt", "Hello, this is a test file.")
    iterate_range(1, 5)
    generator = generate_yields(5)


if __name__ == '__main__':
    main()

