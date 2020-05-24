def areYouPlayingBanjo(name):
    """
    Are You Playing Banjo? Kata
    https://www.codewars.com/kata/53af2b8861023f1d88000832
    """
    return name+' plays banjo' if name[0] == 'R' or name[0] == 'r' else name+' does not play banjo'