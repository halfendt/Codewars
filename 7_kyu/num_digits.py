def digits(n):
    """
    Number of Decimal Digits Kata
    https://www.codewars.com/kata/58fa273ca6d84c158e000052
    """
    num_digits = 0
    while n > 0:
        n = n // 10
        num_digits += 1
    return num_digits