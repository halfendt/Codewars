def century(year):
    """
    Century From Year Kata
    https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097
    """
    return year//100 if year%100 == 0 else year//100+1