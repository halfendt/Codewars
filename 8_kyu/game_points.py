def points(games):
    """
    Total amount of points Kata
    https://www.codewars.com/kata/5bb904724c47249b10000131
    """
    return sum([3 if game[0] > game[-1] else 1 if game[0] == game[-1] else 0 for game in games])