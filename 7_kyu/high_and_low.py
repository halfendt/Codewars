def high_and_low(numbers):
    """
    Highest and Lowest Kata
    https://www.codewars.com/kata/554b4ac871d6813a03000035
    """
    nums = list(map(int, numbers.split()))
    return str(max(nums))+' '+str(min(nums))