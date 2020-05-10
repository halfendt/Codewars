def pig_it(text):
    """
    Simple Pig Latin Kata
    https://www.codewars.com/kata/520b9d2ad5c005041100000f
    """
    return ' '.join(word[1:]+word[0]+'ay' if word.isalpha() else word for word in text.split())