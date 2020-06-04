def race(v1, v2, g):
    """
    Tortoise racing Kata
    https://www.codewars.com/kata/55e2adece53b4cdcb900006c
    """
    if v1 >= v2: return None
    t = g/(v2-v1)
    return [int(t), int((t*60) % 60), int((t*3600) % 60)]