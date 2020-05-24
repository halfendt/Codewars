def decrypt(encrypted_text, n):
    """
    Simple Encryption #1 - Alternating Split Kata
    https://www.codewars.com/kata/57814d79a56c88e3e0000786
    """
    if text in ("", None):
        return text
    
    ind = len(text)//2
    for i in range(n):
        first = text[ind:]
        second = text[:ind]
        text = "".join(first[i:i+1] + second[i:i+1] for i in range(ind+1))
    return text


def encrypt(text, n):
    for _ in range(n):
        text = text[1::2] + text[::2]
    return text
