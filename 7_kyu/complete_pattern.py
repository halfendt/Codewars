def pattern(n):
    """
    Complete The Pattern #1 Kata
    https://www.codewars.com/kata/5572f7c346eb58ae9c000047
    """ 
    return '\n'.join([str(num)*num for num in range(1, n+1)])