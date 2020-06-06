def encrypt_this(text):
    """
    Encrypt this! Kata
    https://www.codewars.com/kata/5848565e273af816fb000449
    """
    res = []
    for word in text.split():
        if len(word) == 1:
            res.append(f'{ord(word[0])}')
        elif len(word) == 2:
            res.append(f'{ord(word[0])}{word[1]}')
        else:
            res.append(f'{ord(word[0])}{word[-1]}{word[2:-1]}{word[1]}')
    return ' '.join(res)