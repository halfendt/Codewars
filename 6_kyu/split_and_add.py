from itertools import zip_longest

def split_and_add(numbers, n):
    """
    Split and then add both sides of an array together Kat
    https://www.codewars.com/kata/5946a0a64a2c5b596500019a
    """
    for _ in range(n):
        numbers = [x+y for x,y in zip_longest(reversed(numbers[:len(numbers)//2]), reversed(numbers[len(numbers)//2:]), fillvalue=0)][::-1]
    return numbers