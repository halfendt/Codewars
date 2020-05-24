def bouncing_ball(h, bounce, window):
    """
    Bouncing Balls Kata
    https://www.codewars.com/kata/5544c7a5cb454edb3c000047
    """
    if h <= 0 or 0 > bounce or bounce >= 1 or window >= h:
        return -1
    num = 1
    while h * bounce > window:
        num +=2
        h *= bounce
    return num