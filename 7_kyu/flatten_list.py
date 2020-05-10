def flatten_me(lst):
    """
    Flatten Me Kata
    https://www.codewars.com/kata/55a5bef147d6be698b0000cd
    """
    return [obj for arg in args for obj in (flatten_me(arg) if isinstance(arg, list) else [arg])]