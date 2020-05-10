def series_sum(n):
    """
    Sum of the first nth term of Series Kata
    https://www.codewars.com/kata/555eded1ad94b00403000071
    """
    return '{:0.2f}'.format(sum(1/(3*num+1) for num in range(n)))