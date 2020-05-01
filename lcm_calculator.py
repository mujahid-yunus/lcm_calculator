import math

"""
    This block of codes takes in any number of numbers and return their LCM
"""


def check_list_divisibility(dividend, divisor):
    for member in divisor:
        if dividend % member != 0:
            return 0
    return 1


def multiplication_list(int_list):
    addition = 1
    for _ in list(int_list):
        addition *= _
    return addition


def lcm_calculator(*args):
    """
    info: returns the lcm of the given numbers
    lcm of a set of numbers is a number which is a multiple of all the numbers
    lcm is the list common divisor of the numbers
    """
    list_args = list(args)
    a = min(list_args)
    b = max(list_args)
    multiples = []
    for _ in range(a, multiplication_list(list_args)):
        if check_list_divisibility(_, list_args) == 1:
            multiples.append(_)
    print(multiples)
    return min(multiples)


print(lcm_calculator(10, 15, 20, 25))
