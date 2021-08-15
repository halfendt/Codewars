import string

def caesar(message, key=1):
    """
    Caeser Encryption Kata
    https://www.codewars.com/kata/56dc695b2a4504b95000004e/
    """
    letters = string.ascii_lowercase
    mask = letters[key:] + letters[:key]
    trantab = str.maketrans(letters, mask)
    return message.translate(trantab).upper()