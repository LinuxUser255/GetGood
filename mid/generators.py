from typing import Iterator

def square_numbers(limit: int) -> Iterator[int]:
    for n in range(limit):
        yield n**2

    for square in square_numbers(5):
        print(square)