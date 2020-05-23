def openOrSenior(data):
    """
    Categorize New Member Kata
    https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa
    """
    return ['Senior' if d[0]>= 55 and d[1]>7 else 'Open' for d in data]