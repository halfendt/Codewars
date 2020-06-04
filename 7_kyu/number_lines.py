def number(lines):
    """
    Testing 1-2-3 Kata
    https://www.codewars.com/kata/54bf85e3d5b56c7a05000cf9
    """
    return [f'{num}: {line}' for num, line in enumerate(lines, 1)]