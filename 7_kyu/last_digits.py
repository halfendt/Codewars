def solution(n,d):
    """
    last digits of a number Kata
    https://www.codewars.com/kata/5cd5ba1ce4471a00256930c0
    """
    if d <= 0:
        return []
    else:
        return [int(num) for num in str(n)[-d:]]