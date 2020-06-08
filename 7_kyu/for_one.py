def one(sq, fun):
    """
    Enumerable Magic #5- True for Just One? Kata
    https://www.codewars.com/kata/54599705cbae2aa60b0011a4
    """
    return sum(map(fun, sq)) == 1