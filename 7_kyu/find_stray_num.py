def stray(arr):
    """
    Find the stray number Kata
    https://www.codewars.com/kata/57f609022f4d534f05000024
    """
    return min(arr, key=arr.count)