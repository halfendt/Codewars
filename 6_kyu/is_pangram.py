from string import ascii_lowercase

def is_pangram(s):
    """
    Detect Pangram Kata
    https://www.codewars.com/kata/545cedaa9943f7fe7b000048
    """
    return sum(True if lett in s.lower() else False for lett in ascii_lowercase) >= 26