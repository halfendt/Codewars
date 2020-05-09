def morse_converter(string):
    """
    Alien Beer Morse Code Kata
    https://www.codewars.com/kata/56dc4f570a10feaf0a000850
    """
    code_to_num = {'1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
                   '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'}
    code_to_num = {code: lett for lett, code in code_to_num.items()}
    return int(''.join(code_to_num[code] for code in [string[ind:ind+5] for ind in range(0, len(string), 5)]))