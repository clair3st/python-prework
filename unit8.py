# TODO: Define a function is_even that will take a number x as input.
# If x is even, then return True.
# Otherwise, return False.
def is_even(x):
    if x%2 == 0:
        return True
    else:
        return False

# TODO: Define a function is_int that takes a number x as an input.
# Have it return True if the number is an integer (as defined above) and False otherwise.
def is_int(x):
    if x%1 == 0: return True
    else: return False

# TODO: Write a function called digit_sum that takes a positive integer n as input and returns the sum of all that number's digits.
# For example: digit_sum(1234) should return 10 which is 1 + 2 + 3 + 4.
def digit_sum(n):
