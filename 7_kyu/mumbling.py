def accum(s):
    """
    Mumbling Kata
    https://www.codewars.com/kata/5667e8f4e3f572a8f2000039
    """
    return '-'.join(char.upper()+char.lower()*ind for ind, char in enumerate(s.lower()))