import re

def count_smileys(arr):
    """
    Count the smiley faces! Kata
    https://www.codewars.com/kata/583203e6eb35d7980400002a
    """
    return len(re.findall('[:;][-~]?[)D]', str(arr)))