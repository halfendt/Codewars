def dig_pow(n, p):
    """
    Playing with digits Kata
    https://www.codewars.com/kata/5552101f47fc5178b1000050
    """
    fac = sum([int(num)**(p+ind) for ind, num in enumerate(str(n))])/n
    return int(fac) if fac % 1 == 0 else -1