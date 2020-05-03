def decode(r):
    """
    Reversing a Process Kata
    https://www.codewars.com/kata/5dad6e5264e25a001918a1fc
    """
    strng = r.lstrip('0123456789')
    num = r[:-len(strng)]
    s = ''
    for letter in strng:
        char = ord(letter)-97
        comb_char = [org_num*int(num)%26 for org_num in range(26)]
        if comb_char.count(char) == 1:
            s += chr(comb_char.index(char)+97)
        else:
            return 'Impossible to decode'
    return s