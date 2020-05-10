def validate_pin(pin):
    """
    Regex validate PIN code Kata
    https://www.codewars.com/kata/55f8a9c06c018a0d6e000132
    """
    return len(pin) in (4, 6) and pin.isdigit()