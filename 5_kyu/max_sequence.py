def max_sequence(arr):
    """
    Maximum subarray sum Kata
    https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c
    """
    max_res, curr = 0, 0
    for x in arr:
        curr += x
        if curr < 0:
            curr = 0
        if curr > max_res:
            max_res = curr
    return max_res