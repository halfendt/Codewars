def longest(s1, s2):
    """
    Two to One Kata
    https://www.codewars.com/kata/5656b6906de340bd1b0000ac
    """
    return ''.join(sorted(set(s1+s2)))