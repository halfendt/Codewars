import re

def decipher_this(string):
    """
    Decipher this! Kata
    https://www.codewars.com/kata/581e014b55f2c52bb00000f8
    """
    res = []
    for word in string.split():
        f = chr(int(re.findall(r'\d+', word)[0]))
        rest = re.findall(r'[A-Za-z]+', word)
        if rest == []:
            res.append(f)
        elif len(rest[0]) == 1:
            res.append(f+rest[0][0])
        else:
            res.append(f+rest[0][-1]+rest[0][1:-1]+rest[0][0])
    return ' '.join(res)