def remove_smallest(numbers):
    """
    Remove the minimum Kata
    https://www.codewars.com/kata/563cf89eb4747c5fb100001b
    """
    nums = numbers[:]
    if nums: nums.remove(min(nums))
    return nums