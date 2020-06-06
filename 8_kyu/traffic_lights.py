def update_light(current):
    """
    Thinkful - Logic Drills: Traffic light Kata
    https://www.codewars.com/kata/58649884a1659ed6cb000072
    """
    return {'green': 'yellow', 'yellow': 'red', 'red': 'green'}[current]