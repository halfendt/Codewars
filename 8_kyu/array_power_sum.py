def array_madness(a,b):
    """
    SpeedCode #2 - Array Madness Kata
    https://www.codewars.com/kata/56ff6a70e1a63ccdfa0001b1
    """
    return sum(num**2 for num in a) > sum(num**3 for num in b)