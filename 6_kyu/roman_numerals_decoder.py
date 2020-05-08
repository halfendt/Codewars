def solution(roman):
    """
    Roman Numerals Decoder Kata
    https://www.codewars.com/kata/51b6249c4612257ac0000005
    """
    sym_val = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X',
               9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    if not roman:
        return 0
    for value, sym in sym_val.items():
        if roman.startswith(sym):
            return value + solution(roman[len(sym):])