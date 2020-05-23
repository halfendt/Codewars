def count_sheep(n):
    """
    If you can't sleep, just count sheep!! Kata
    https://www.codewars.com/kata/5b077ebdaf15be5c7f000077
    """
    return ''.join("{} sheep...".format(i+1) for i in range(n))