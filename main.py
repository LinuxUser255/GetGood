#!/usr/bin/env python3

# This main.py ties together all the basic examples
from basic_control_flow_example import run_it
from functions import run_funcs
from case_switch_example import case_switch
from list_comprehension_example import list_comprehension_example
from regex_example import regex_example
from variables_and_data_types import data_types
from dictionaries import dictionary_example
from mid.comprehensions import comp_squares, cube_numbers, get_even_numbers
from mid.generators import square_numbers


def main():
    run_it()
    run_funcs()
    case_switch()
    dictionary_example()
    list_comprehension_example()
    regex_example()
    data_types()
    comp_squares()
    cube_numbers()
    get_even_numbers()
    square_numbers(limit=5)


if __name__ == '__main__':
    main()
