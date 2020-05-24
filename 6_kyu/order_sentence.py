import re

def order(sentence):
    """
    Your order, please Kata
    https://www.codewars.com/kata/55c45be3b2079eccff00010f
    """
    return ' '.join(elem[1] for elem in sorted({re.findall("\d+", word)[0]: word for word in sentence.split()}.items()))