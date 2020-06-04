def revrot(strng, sz):
    """
    Reverse or rotate? Kata
    https://www.codewars.com/kata/56b5afb4ed1f6d5fb0000991
    """
    new_strng = ''
    if strng == '' or sz <= 0: return ''
    for i in range(len(strng)//sz):
        chunk = strng[sz*i:sz*(i+1)]
        if sum(int(digit)**3 for digit in chunk)%2 == 0:
            new_strng += chunk[::-1]
        else:
            new_strng += chunk[1:]+chunk[0]
    return new_strng