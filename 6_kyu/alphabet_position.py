def alphabet_position(text):
    """
    Replace With Alphabet Position Kata
    https://www.codewars.com/kata/546f922b54af40e1e90001da
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return ' '.join([str(i+1) for char in text for i, lett in enumerate(alphabet) if char.lower() == lett])