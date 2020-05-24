def find(n):
    """
    Sum of all the multiples of 3 or 5 Kata
    https://www.codewars.com/kata/57f36495c0bb25ecf50000e7
    """
    return sum(i for i in range(n+1) if i%3 == 0 or i%5 == 0)