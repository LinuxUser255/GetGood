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
        return 'Polynomial({!r})'.format(self.coefficients)

    def __add__(self, other): # add is implemented by adding up some components
        return Polynomial([a + b for a, b in zip(self.coefficients, other.coefficients)])

    def __len__(self):
        return len(self.coefficients) # len is implemented by being called on a constituent object

    def __call__(self, x):
        # Evaluate the polynomial at value x
        result = 0
        for i, coeff in enumerate(self.coefficients):
            result += coeff * (x ** i)
        return result


# Create polynomial objects. Insert breakpoint at p1 to observe the representation of these objects.
p1 = Polynomial([1, 2, 3])  # represents 1 + 2x + 3x²
p2 = Polynomial([3, 4, 3])  # represents 3 + 4x + 3x²

# Using __repr__ method
print("=== __repr__ method ===")
print(repr(p1))  # Calls p1.__repr__()
print(repr(p2))  # Calls p2.__repr__()

# Using __add__ method
print("\n=== __add__ method ===")
p3 = p1 + p2  # Calls p1.__add__(p2)
print(f"p1: {p1}")
print(f"p2: {p2}")
print(f"p1 + p2: {p3}")  # Should be [4, 6, 6] representing 4 + 6x + 6x²

# Using __len__ method
print("\n=== __len__ method ===")
print(f"Length of p1: {len(p1)}")  # Calls p1.__len__()
print(f"Length of p2: {len(p2)}")  # Calls p2.__len__()

# Using __call__ method
print("\n=== __call__ method ===")
x = 2
print(f"p1({x}) = {p1(x)}")  # Calls p1.__call__(2) - evaluates 1 + 2(2) + 3(2²) = 1 + 4 + 12 = 17
print(f"p2({x}) = {p2(x)}")  # Calls p2.__call__(2) - evaluates 3 + 4(2) + 3(2²) = 3 + 8 + 12 = 23

# Demonstrating all methods together
print("\n=== Combined example ===")
result = p1 + p2  # __add__
print(f"Result polynomial: {result}")  # __repr__
print(f"Result has {len(result)} coefficients")  # __len__
print(f"Result evaluated at x=3: {result(3)}")  # __call__