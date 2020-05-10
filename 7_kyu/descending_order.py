def descending_order(num):
    """
    Descending Order Kata
    https://www.codewars.com/kata/5467e4d82edf8bbf40000155
    """
    return int(''.join(sorted(str(num), reverse=True)))