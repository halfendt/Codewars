def is_valid_walk(walk):
    """
    Take a Ten Minute Walk Kata
    https://www.codewars.com/kata/54da539698b8a2ad76000228
    """
    if len(walk) != 10:
        return False
    num_n = 0
    num_s = 0
    num_e = 0
    num_w = 0
    
    for trip in walk:
        if trip == 'n':
            num_n += 1
        elif trip == 's':
            num_s += 1
        elif trip == 'e':
            num_e += 1
        elif trip == 'w':
            num_w += 1
    
    if num_n == num_s and num_e == num_w:
        return True
    else:
        return False