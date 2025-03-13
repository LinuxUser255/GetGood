def comp_squares():
    """
    Generates a list of squares of even numbers from 0 to 9 using a list comprehension.
    Uses PEMDAS (Parentheses, Exponents, Multiplication and Division, Addition and Subtraction)
    
    This function creates a list containing the squares of even numbers
    from 0 to 9 (inclusive) using a list comprehension. It then prints
    the resulting list.
    
    The list comprehension works as follows:
    - Iterates over numbers 0 to 9
    - Filters for even numbers (x % 2 == 0)
    - Squares each even number (x**2)
    - Collects the results in a list
    
    Returns:
    None. The function prints the resulting list.
    """
    print("list comprehension example:")
    squares = [x**2 for x in range(10) if x % 2 == 0]
    print(squares)
    print()
    # [0, 4, 16, 36, 64]
    
# Dictionary comprehension example
def cube_numbers():
    print("dictionary comprehension example:")
    cubes = {x: x**3 for x in range(5)}
    print(cubes)
    # [0, 4, 16, 36, 64]
    # {0: 0, 1: 1, 2: 8, 3: 27, 4: 64}
    
# Example of a set comprehension
def get_even_numbers():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    evens = {num for num in numbers if num % 2 == 0}
    print(evens)
    # {2, 4, 6, 8, 10}