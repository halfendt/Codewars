def disemvowel(string):
    """
    Disemvowel Trolls Kata
    https://www.codewars.com/kata/52fba66badcd10859f00097e
    """
    vowel = 'aeiouAEIOU'
    stringg = ''
    for char in string:
        if char not in vowel:
            stringg += char
    return stringg