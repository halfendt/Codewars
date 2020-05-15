def is_isogram(string):
    """
    Isograms Kata
    https://www.codewars.com/kata/54ba84be607a92aa900000f1
    """
    for char in string:
        if string.count(char) > 1:
            return False
    return True