def reverse_words(text):
    """
    Reverse words Kata
    https://www.codewars.com/kata/5259b20d6021e9e14c0010d4
    """
    return ' '.join(t[::-1] for t in text.split(' ')) 