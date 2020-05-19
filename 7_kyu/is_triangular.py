import math

def is_triangular(t):
    """
    Beginner Series #5 Triangular Numbers Kata
    https://www.codewars.com/kata/56d0a591c6c8b466ca00118b
    """
    return math.ceil((-1+math.sqrt(1 + 8*t))/2 % 1) == 0
