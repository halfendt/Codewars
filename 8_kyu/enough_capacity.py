def enough(cap, on, wait):
    """
    Will there be enough space? Kata
    https://www.codewars.com/kata/5875b200d520904a04000003
    """
    return 0 if wait < cap-on else wait-cap+on