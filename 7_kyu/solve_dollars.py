def solve(n):
    """
    ATM Kata
    https://www.codewars.com/kata/5635e7cb49adc7b54500001c
    """
    total = 0
    for bills in [500, 200, 100, 50, 20, 10]:
        div, rem = divmod(n, bills)
        total += div
    if rem: return -1
    return t