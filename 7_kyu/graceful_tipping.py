from math import ceil, log10

def graceful_tipping(bill):
    """
    Graceful Tipping Kata
    https://www.codewars.com/kata/5eb27d81077a7400171c6820
    """
    bill *= 1.15
    mult = 1 if bill < 10 else 5*10**int(log10(bill)-1)
    return ceil(bill/mult)*mult