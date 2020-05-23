def rps(p1, p2):
    """
    Rock Paper Scissors! Kata
    https://www.codewars.com/kata/5672a98bdbdd995fad00000f
    """
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[p1] == p2:
        return "Player 1 won!"
    if beats[p2] == p1:
        return "Player 2 won!"
    return "Draw!"