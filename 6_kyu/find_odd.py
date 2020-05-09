def find_it(seq):
    """
    Find the odd int Kata
    https://www.codewars.com/kata/54da5a58ea159efa38000836
    """
    return [num for num in seq if seq.count(num)%2][0]