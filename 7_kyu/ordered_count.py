from collections import Counter

def ordered_count(inp):
    """
    Ordered Count of Characters Kata
    https://www.codewars.com/kata/57a6633153ba33189e000074
    """
    return list(Counter(inp).items())