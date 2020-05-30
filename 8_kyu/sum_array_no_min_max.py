def sum_array(arr):
    """
    Sum without highest and lowest number Kata
    https://www.codewars.com/kata/576b93db1129fcf2200001e6
    """
    return sum(sorted(arr)[1:-1]) if arr != None else 0