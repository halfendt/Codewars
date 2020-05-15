def to_jaden_case(string):
    """
    Jaden Casing Strings Kata
    https://www.codewars.com/kata/5390bac347d09b7da40006f6
    """
    return ' '.join(word.capitalize() for word in string.split())