def find_nb(m):
    """
    Build a pile of Cubes Kata
    https://www.codewars.com/kata/5592e3bd57b64d00f3000047
    """
    n = 0
    while m > 0:
        n += 1
        m -= n**3
    if m == 0:
        return n
    return -1