from collections import Counter
from itertools import compress

def anagrams(word, words):
    """
    Where my anagrams at? Kata
    https://www.codewars.com/kata/523a86aa4230ebb5420001e1
    """
    return list(compress(words, [True if Counter(word) == Counter(ele) else False for ele in words]))      