def binary_array_to_number(arr):
    """
    Ones and Zeros Kata
    https://www.codewars.com/kata/578553c3a1b8d5c40300037c
    """
    return int(''.join(map(str, arr)),2)