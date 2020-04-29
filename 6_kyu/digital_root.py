def digital_root(n):
    """
    Sum of Digits / Digital Root Kata
    https://www.codewars.com/kata/541c8630095125aba6000c00
    """
    if n < 10:
        return n
    else:
        return digital_root(sum([int(num) for num in str(n)]))