def count_up_to(max_value):
    """
    A generator function that yields numbers from 1 up to max_value.

    This function creates a generator that produces a sequence of integers
    starting from 1 and continuing up to and including the specified max_value.
    It's memory-efficient for large ranges as it generates values on-the-fly.

    Parameters:
    max_value (int): The upper limit of the sequence (inclusive).
                     Must be a positive integer.

    Yields:
    int: The next integer in the sequence, starting from 1 and
         going up to max_value.

    Example:
    >>> for num in count_up_to(5):
    ...     print(num)
    1
    2
    3
    4
    5
    """
    current = 1
    while current <= max_value:
        yield current  # Yield the current value and pause execution
        current += 1  # Increment the current value


if __name__ == "__main__":
    counter = count_up_to(10000000)

    for number in counter:
        print(number)

# Generators are used when you want a space efficient way of code execution,
# or calculating large results that don't fit into memory.
# This generator perform a calculation on the specific value, needed  at that time
# saves memory by not storing all the results in memory at once.