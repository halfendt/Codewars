from random import random

def mutate(chromosome, p):
    """
    Genetic Algorithm Series - #2 Mutation Kata
    https://www.codewars.com/kata/567b39b27d0a4606a5000057
    """
    code = {'0':'1', '1':'0'}
    return ''.join(code[num] if random() < p else num for num in chromosome)