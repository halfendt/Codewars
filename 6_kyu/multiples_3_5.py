def solution(number):
    """
    Multiples of 3 or 5 Kata
    https://www.codewars.com/kata/514b92a657cdc65150000006
    """
    return sum([num for num in range(number) if num %3 == 0 or num %5 == 0])