def derive(coefficient, exponent):
    """
    Take the Derivative Kata
    https://www.codewars.com/kata/5963c18ecb97be020b0000a2
    """
    return str(coefficient*exponent)+'x^'+str(exponent - 1)