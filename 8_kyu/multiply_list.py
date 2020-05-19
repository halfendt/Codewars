from functools import reduce

def multiply(arr):
    """
    Beginner - Reduce but Grow Kata
    https://www.codewars.com/kata/57f780909f7e8e3183000078
    """
    return reduce(lambda a, b: a * b, arr)
