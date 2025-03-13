#!/usr/bin/env python3

# https://docs.python.org/3.11/reference/datamodel.html
# Data model methods, (aka dunder methods)
# The pattern: some behaviour that I want to implement -> write some __function__
# The pattern that we see is: the python data model, is a means by which you can implement protocols
# those protocols have some abstract meaning, depending on the object it's self.

# This is a very common pattern in the Python data model.
# When you want to implement a custom behaviour on a custom object,
# we do it by implementing an underscore function,
# which ties to some top-level syntax, or, some top-level function,
# and we implement it in terms of that thing it's self.

# For OOP in Python, there are three core patterns that you must really understand:
# 1. The Protocol view of Python.
# 2. The built-in inheritance protocol. And, how it works. (where you go on a Python Object to look for things)
# 3. Caveats around how Object orientation of Python works.

# This is the Protocol view of Python.
class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients


    def __repr__(self): # implemented by calling __repr__ on some component
        return 'Polynomial(*{!r})'.format(self.coefficients)

    def __add__(self, other): # add is implemented by adding up some components
        return Polynomial([a + b for a, b in zip(self.coefficients, other.coefficients)])

    def __len__(self):
        return len(self.coefficients) # len is implemented by being called on a constituent object

    def __call__(self, *args, **kwargs):
        pass


p1 = Polynomial([1, 2, 3])
p2 = Polynomial([3, 4, 3])





