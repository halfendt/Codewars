def find_short(s):
    """
    Shortest Word Kata
    https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9
    """
    return min(len(word) for word in s.split())