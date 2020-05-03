def power_sumDigTerm(n):
    """
    Numbers that are a power of their sum of digits Kata
    https://www.codewars.com/kata/55f4e56315a375c1ed000159
    """
    return sorted(a**b for a in range(2, 200) for b in range(2, 20) if a == sum(map(int, str(a**b))))[n-1]