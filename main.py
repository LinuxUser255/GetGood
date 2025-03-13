#!/usr/bin/env python3

from mid.comprehensions import comp_squares
from mid.comprehensions import cube_numbers
from mid.comprehensions import get_even_numbers
from mid.generators import square_numbers

def main():
    comp_squares()
    cube_numbers()
    get_even_numbers()
    # call the generator function from generators.py
    square_numbers(limit=5)


if __name__ == '__main__':
    main()

