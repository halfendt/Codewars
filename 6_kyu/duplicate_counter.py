from collections import Counter

def duplicate_count(text):
    """
    Counting Duplicates Kata
    https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1
    """
    return len([k for k, v in dict(Counter(text.lower())).items() if v > 1])