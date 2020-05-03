def halving_sum(n):
    """
    Halving Sum Kata
    https://www.codewars.com/kata/5a58d46cfd56cb4e8600009d
    """
    return n if n == 1 else halving_sum(n//2) + n