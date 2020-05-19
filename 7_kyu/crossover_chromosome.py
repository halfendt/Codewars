def crossover(chromosome1, chromosome2, index):
    """
    Genetic Algorithm Series - #3 Crossover Kata
    https://www.codewars.com/kata/567d71b93f8a50f461000019
    """
    return [chromosome1[:index] + chromosome2[index:], chromosome2[:index] + chromosome1[index:]]