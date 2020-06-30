def arithmetic(a, b, operator):
    """
    Make a function that does arithmetic! Kata
    https://www.codewars.com/kata/583f158ea20cfcbeb400000a
    """
    op_dict = {'add': '+', 'subtract': '-', 'multiply': '*', 'divide': '/'}
    return eval(f'{a}{op_dict[operator]}{b}')