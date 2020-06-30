import numpy as np

def find_next_square(sq):
    """
    Find the next perfect square! Kata
    https://www.codewars.com/kata/56269eb78ad2e4ced1000013
    """
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1)**2
    return -1