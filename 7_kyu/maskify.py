def maskify(cc):
    """
    Credit Card Mask Kata
    https://www.codewars.com/kata/5412509bd436bd33920011bc
    """
    return '#'*(len(cc)-4)+cc[-4:]