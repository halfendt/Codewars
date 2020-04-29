def find_missing_letter(chars):
    """
    Find the missing letter
    https://www.codewars.com/kata/5839edaa6754d6fec10000a2
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    for i, lett in enumerate(alphabet):
        if lett in chars:
            if alphabet[i+1] not in chars:
                return alphabet[i+1]