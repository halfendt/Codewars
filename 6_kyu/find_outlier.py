def find_outlier(integers):
    """
    Find The Parity Outlier Kata
    https://www.codewars.com/kata/5526fc09a1bbd946250002dc
    """
    zero_one = [num%2 for num in integers]
    return integers[zero_one.index(1)] if zero_one.count(1) == 1 else integers[zero_one.index(0)]