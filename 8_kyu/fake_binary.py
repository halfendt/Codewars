def fake_bin(x):
    """
    Fake Binary Kata
    https://www.codewars.com/kata/57eae65a4321032ce000002d
    """
    return ''.join('0' if int(num) < 5 else '1' for num in x)