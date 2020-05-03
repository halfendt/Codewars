def split_in_parts(s, part_length):
    """
    Split In Parts Kata
    https://www.codewars.com/kata/5650ab06d11d675371000003
    """
    strng = ''
    while len(s) > 0:
        strng += s[:part_length] + ' '
        s = s[part_length:]
    return strng[:-1]