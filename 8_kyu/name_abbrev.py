def abbrevName(name):
    """
    Abbreviate a Two Word Name Kata
    https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3
    """
    return '.'.join([name.split()[0][0].upper(), name.split()[1][0].upper()])