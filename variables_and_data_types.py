#!/usr/bin/env python3

# various data types
def data_types():
    # string example
    text = "this is a test string"

    # this is an integer number example
    number = 10

    # float is a floating-point number-decimal number
    decimal = 3.14

    # boolean example
    uses_linux = True
    does_not_use_linux = False

    # Tuple example is inmutable (cannot be changed once created)
    tuple_example = (1, "two", 5.5)

    # list example
    names = ['Chris', 'Emily', 'John']

    # a set example. Cannot contain duplicate values and is unordered
    set_example_one = {1, 2, 3, 4, 5}
    set_example_two = {11, 9, 10, 8, 7}

    # dictionary example. Key-value pairs, that must be in quotes
    transportation = {"car": "toyota", "motorcycle": "honda", "bike": "kawasaki"}

    # data type conversion examples
    print('example of converting string to integer')
    number_as_string = '20'
    print(number_as_string)

    # convert string to integer
    print('example of converting integer to string using the int() function')
    converted_number = int(number_as_string)
    print(converted_number)

    # convert integer to float
    print('example of converting integer to float')
    # convert integer to float
    print('example of converting integer to float')
    converted_decimal = float(converted_number)
    print(converted_decimal)

    # type hinting
    age: int = 30
    name: str = 'John'
    print(f'Name: {name}, Age: {age}')

data_types()


































