def spin_words(sentence):
    """
    Stop gninnipS My sdroW! Kata
    https://www.codewars.com/kata/5264d2b162488dc400000001
    """
    return ' '.join([word[::-1] if len(word) >= 5 else word for word in sentence.split()])