def get_sum(a,b):
    """
    Beginner Series #3 Sum of Numbers Kata
    https://www.codewars.com/kata/55f2b110f61eb01779000053
    """
    return sum(range(b,a+1)) if a > b else sum(range(a,b+1))