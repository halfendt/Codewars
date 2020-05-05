def find_all(array, n):
    """
    Find all occurrences of an element in an array Kata
    https://www.codewars.com/kata/59a9919107157a45220000e1
    """
    return [index for index, item in enumerate(array) if item == n]