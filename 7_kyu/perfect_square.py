def square_it(digits):
    """
    Perfect squares, perfect fun
    https://www.codewars.com/kata/5705ca6a41e5be67720012c0
    """
    len_digits = len(str(digits))
    root = len_digits ** 0.5
    if len_digits == int(root + 0.5) ** 2:
        return '\n'.join([str(digits)[i:i+len_digits//int(root)] for i in range(0, len_digits, len_digits//int(root))])
    else:
        return 'Not a perfect square!'