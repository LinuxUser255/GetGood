#!/usr/bin/env python3

"""
1. Meta Class
2. Decorator
3. Generator
4. Context Manager
"""

# def about_symposium():
def symposium():
    print("James Powell presents four important features of Python:")

# data modelling
def data_model():
    print("Data Modeling")


def decorators_example(func):
    print(f"Decorators")


def generators_example():
    print("Generators")


def context_manager():
    print("Context Manager")


def main():
    data_model()
    decorators_example(data_model)
    generators_example()
    context_manager()


if __name__ == "__main__":
    main()

