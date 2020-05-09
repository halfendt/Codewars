from re import compile

def decodeBits(bits):
    """
    Decode the Morse code, advanced Kata
    https://www.codewars.com/kata/54b72c16cd7f5154e9000457
    """
    tokens = compile('(0+)').split(bits.strip('0'))
    lenDot = min(len(token) for token in tokens)
    lenDash = 3 * lenDot

    code = []
    for token in tokens:
        if token[0] == '1':
            code.append('.' if len(token) < lenDash else '-')
        elif len(token) > lenDot:
            code.append(' ' if len(token) <= lenDash else '   ')
    return ''.join(code)
    
def decodeMorse(morseCode):
    return ' '.join(''.join(MORSE_CODE[code] for code in word.split()) for word in morseCode.strip().split('   '))
