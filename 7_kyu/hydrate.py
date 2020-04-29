def hydrate(drink_string): 
    """
    Responsible Drinking Kata
    https://www.codewars.com/kata/5aee86c5783bb432cd000018
    """
    numbers = '123456789'
    glasses = 0

    for char in drink_string:
        if char in numbers:
            glasses += int(char)
    if glasses == 1:
         return str(glasses)+' glass of water'
    else:
        return str(glasses)+' glasses of water'