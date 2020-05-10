import re

def calculate_string(st):
    """
    Basics 03: Strings, Numbers and Calculation Kata
    https://www.codewars.com/kata/56b5dc75d362eac53d000bc8
    """
    return str(round(eval(re.sub('[^0-9\-\+\*\/\.]',"",st))))