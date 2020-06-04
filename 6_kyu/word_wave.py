def wave(people):
    """
    Mexican Wave Kata
    https://www.codewars.com/kata/58f5c63f1e26ecda7e000029
    """
    return [people[:i]+lett.upper()+people[i+1:] for i, lett in enumerate(people) if lett != ' ']