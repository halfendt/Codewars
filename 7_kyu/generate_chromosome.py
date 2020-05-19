from random import randint

def generate(length):
    """
    Genetic Algorithm Series - #1 Generate Kata
    https://www.codewars.com/kata/567d609f1c16d7369c000008
    """
    return ''.join(str(randint(0,1)) for _ in range(length))