def digitize(n):
    """
    Convert number to reversed array of digits Kata
    https://www.codewars.com/kata/5583090cbe83f4fd8c000051
    """
    return list(map(int, str(n)[::-1]))