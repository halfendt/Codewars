def gimme(input_array):
    """
    Find the middle element Kata
    https://www.codewars.com/kata/545a4c5a61aa4c6916000755
    """
    return input_array.index(sorted(input_array)[1])
    