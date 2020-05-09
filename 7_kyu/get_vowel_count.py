def getCount(inputStr):
    """
    Vowel Count
    https://www.codewars.com/kata/54ff3102c1bad923760001f3
    """
    return len([char for char in inputStr if char in 'aeiou'])