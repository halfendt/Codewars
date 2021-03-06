from re import finditer

def differentiate(equation, point):
    """
    Differentiate a polynomial Kata
    https://www.codewars.com/kata/566584e3309db1b17d000027
    """
    res = 0
    for exp in finditer(r'([\+\-])?(\d*)?x\^?(\d+)?', equation):
        sign = -1 if exp.group(1) == '-' else 1
        scalar = int(exp.group(2)) if exp.group(2) else 1
        power = int(exp.group(3)) if exp.group(3) else 1
        res += sign * (power * scalar) * point ** (power - 1)
    return res