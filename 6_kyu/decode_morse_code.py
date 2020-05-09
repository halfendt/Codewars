def decodeMorse(morse_code):
    """
    Decode the Morse code Kata
    https://www.codewars.com/kata/54b724efac3d5402db00065e
    """
    MORSE_CODE = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 
                  'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-',
                  'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....',
                  '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----', ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.',
                  '-':'-....-', '(':'-.--.', ')':'-.--.-'}
    MORSE_CODE = {code: lett for lett, code in MORSE_CODE.items()}
    return ' '.join(''.join(MORSE_CODE[code] for code in word.split()) for word in morse_code.strip().split('   '))