def solution(n):
    """
    Roman Numerals Encoder Kata
    https://www.codewars.com/kata/51b62bf6a9c58071c600001b
    """
    sym_val = {1000:'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X',
               9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    if n == 0: return ""
    return next(k + solution(n-v) for v, k in sym_val.items() if v <= n)