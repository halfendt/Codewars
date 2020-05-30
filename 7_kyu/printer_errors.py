def printer_error(s):
    """
    Printer Errors
    https://www.codewars.com/kata/56541980fa08ab47a0000040
    """
    num = len([char for char in s if char in 'nopqrstuvwxyz'])
    return f'{num}/{len(s)}'