def persistence(n):
    """
    Persistent Bugger Kata
    https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec
    """
    t = 0
    while n >= 10:
        t += 1
        n = eval('*'.join(char for char in str(n)))
    return t