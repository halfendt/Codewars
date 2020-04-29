def find_missing_number(numbers):
    """
    Number Zoo Patrol Kata
    https://www.codewars.com/kata/5276c18121e20900c0000235
    """
    if numbers == []:
        return 1
    value = sum(range(1, max(numbers) + 1)) - sum(numbers)
    if value == 0:
        return len(numbers)+1
    else:
        return value