def generate_hashtag(s):
    """
    The Hashtag Generator Kata
    https://www.codewars.com/kata/52449b062fb80683ec000024
    """
    string = ''.join([word.capitalize() for word in s.split()])
    if len(string) > 140 or len(string) == 0:
        return False
    else:
        return '#'+string