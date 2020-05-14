def sum_two_smallest_numbers(numbers):
    """
    Sum of two lowest positive integers Kata
    https://www.codewars.com/kata/558fc85d8fd1938afb000014
    """
    return sum(sorted(numbers)[:2])