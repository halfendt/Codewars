def count_positives_sum_negatives(arr):
    """
    Count of positives / sum of negatives Kata
    https://www.codewars.com/kata/576bb71bbbcf0951d5000044
    """
    return [len([pos for pos in arr if pos > 0]), sum(neg for neg in arr if neg < 0)] if arr != [] else  []