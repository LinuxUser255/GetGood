#!/usr/bin/env python3

# fizz buzz program
def fizz_buzz(num):
    for num in range(1, 10):
        # is the number divisible by both 3 and 5?
        if num % 5 == 0 and num % 3 == 0:
            # if so, print "FizzBuzz" (Fizz Buzz together)
            print("FizzBuzz")
        elif num % 3 == 0:
            # is the number divisible by 3?  If so, print "Fizz"
            print("Fizz")
        elif num % 5 == 0:
            # is the number divisible by 5?  If so, print "Buzz"
            print("Buzz")
        else:
            # if the number is not divisible by either 3 or 5, print the number itself
            print(num)


# do the Fibonacci Generator
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# call the fizz_buzz function with the first 10 numbers
fizz_buzz(10)

# call the fibonacci generator and print the first 10 numbers
print('Fibonacci:', list(fibonacci(10)))