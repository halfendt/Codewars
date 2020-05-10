def flatten(*args):
    """
    flatten() Kata
    https://www.codewars.com/kata/513fa1d75e4297ba38000003
    """
    return [obj for arg in args for obj in (flatten(*arg) if isinstance(arg, list) else [arg])]