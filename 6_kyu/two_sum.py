def two_sum(numbers, target):
    """
    Two Sum Kata
    https://www.codewars.com/kata/52c31f8e6605bcc646000082
    """
    h = {}
    for i, num in enumerate(numbers):
        n = target - num
        if n not in h:
            h[num] = i
        else:
            return [h[n], i]