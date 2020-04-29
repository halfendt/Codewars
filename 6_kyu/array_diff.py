def array_diff(a, b):
    """
    Array.diff Kata
    https://www.codewars.com/kata/523f5d21c841566fde000009
    """
    return [num for num in a if num not in a or num not in b]