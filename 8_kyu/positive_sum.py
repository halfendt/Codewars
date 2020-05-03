def positive_sum(arr):
    """
    Sum of positive Kata
    https://www.codewars.com/kata/5715eaedb436cf5606000381
    """
    return sum(num if num > 0 else 0 for num in arr)