def black_or_white_key(key_press_count):
    """
    Piano Kata, Part 1
    https://www.codewars.com/kata/589273272fab865136000108
    """
    keyboard = ['white', 'black', 'white', 'white', 'black', 'white', 'black', 'white', 'white', 'black', 'white', 'black']
    return keyboard[(key_press_count - 1) % 88 % 12]