#!/usr/bin/env python3

from typing import List, Tuple, Set, Dict, Union

# Description: This script is about demonstrating various data types in Python.
def about() -> None:
    message: str = 'This script is about demonstrating various data types in Python.'
    print(f'{message}\n')

# printing a string example
def string_example() -> None:
    print('This is a test string')
    print()

# this is an integer number example
def integer_example() -> None:
    number: int = 10
    print(f'Example of an Integer: {number}')
    print()

## float is a floating-point number-decimal number
def float_example() -> None:
    decimal: float = 3.14
    print(f'This is an Example of a Float/Decimal: {decimal}')
    print()

# boolean example
def boolean_example() -> None:
    user: str = 'Me'
    uses_linux: bool = True
    print('This is an example of a Boolean:')
    print(f'{user}: uses Linux: {uses_linux}')
    print()

## list example & list comprehension
def list_example() -> None:
    names: List[str] = ['Christopher', 'Emily', 'John']
    long_names: List[str] = [name for name in names if len(name) > 6]
    print(f'Example of a list: {names}')
    print(f'Long names: {long_names}')
    print()

## Tuple example. A tuple is immutable (cannot be changed once created)
def tuple_example() -> None:
    this_tuple: Tuple[int, str, float] = (1, "two", 5.5)
    print(f'A tuple goes in parentheses: {this_tuple}')
    print()

# Example of a set. It Cannot contain duplicate values and is unordered
def example_of_a_set() -> None:
    example_set: Set[int] = {1, 2, 3, 4, 5}
    example_set.add(6)
    print(f'This is an example of a set: {example_set}')
    print()

# dictionary example. Key-value pairs, that must be in quotes
def example_of_a_dict() -> None:
    vehicles: Dict[str, str] = {"car": "toyota", "motorcycle": "honda", "truck": "ford"}
    print(f'Example of a dictionary: {vehicles}')
    print()

# data type conversion examples
def convert_string_to_integer() -> None:
    string_number: str = '20'
    print(f'Converting a string to an integer: {string_number}')
    print()

# converting integer to string using the int() function
def convert_integer_to_string() -> None:
    integer_number: int = 20
    # use f string format to display the integer as a string
    print(f'Converting an int to a str: {integer_number}')
    print()

def type_hinting_example(age: int, name: str) -> None:
    print(f"Dude's name is {name}, & age is {age}")
    print(f"Type hinting looks like this: age: int, name: str -> None")
    print()

def add(a: float, b: float) -> float:
    return a + b

def for_loop_example() -> None:
    print("For loop example")
    print(20*"-")
    for i in range(5):
        print(f'Current number is: {i}')
        print("The counting begins with 0")

def while_loop_example() -> None:
    print("While loop example\n")
    i: int = 0
    while i < 5:
        print(f'Current number is: {i}')
        i += 1
        print("The counting begins with 0")

# control flow examples
def control_flow() -> None:
    print("Control flow examples\n")
    user_input: str = 'hello'

    if user_input == 'hello':
        print('Bot: Hello, user!')
    elif user_input == 'how are you?':
        print('Bot: I am doing well, thank you!')
    else:
        print('Bot: I don\'t understand that')

def exception_handling() -> None:
    print()
    print("Exception handling example\n")
    try:
        number: int = int('not a number')
        print(f'This will cause an error: {number}')
    except ValueError as e:
        print(f'Caught an exception: {e}')
    finally:
        print('This will always run.')
        print()

def control_flow_user_input() -> None:
    bot_name: str = 'Bot'
    print(f'{bot_name}: How are you?')

    while True:
        usr_input: str = input(f"'Say hi to {bot_name}':  ").lower()

        # if the user input is in the list of greetings, respond with a greeting
        if usr_input in ['hello', 'hi', 'hey']:
            print(f'{bot_name}:  "Hello. How can I help you?"')
        elif usr_input in ['goodbye', 'bye', 'exit']:
            print(f'{bot_name}:  "Goodbye. Have a great day!"')
        elif usr_input in['+', 'add']:
            print(f'{bot_name}: Okay, let\'s add those numbers. Enter two numbers separated by a space.')
            try:
                num1: float = float(input('First number: '))
                num2: float = float(input('Second number: '))
                print(f'The sum is: {num1 + num2}')
            except ValueError:
                print(f'{bot_name}: Invalid input. Please enter a number.')
        else:
            print(f'{bot_name}: I don\'t understand that. Please say hello, goodbye, or type in an addition command.')

# Main entry point for the script.
def main() -> None:
    about()
    string_example()
    integer_example()
    float_example()
    boolean_example()
    tuple_example()
    list_example()
    tuple_example()
    example_of_a_set()
    example_of_a_dict()
    convert_string_to_integer()
    convert_integer_to_string()
    type_hinting_example(30, 'John')
    for_loop_example()
    while_loop_example()
    exception_handling()
    control_flow_user_input()

if __name__=='__main__':
    main()