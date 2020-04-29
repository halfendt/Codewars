def pin_validator(pin):
    """
    Mobile Pin Validator Kumite
    https://www.codewars.com/kumite/5ea31028ac9b310015c67bf5?sel=5ea761b035f6b60032b21046
    """
    return len(str(pin)) == 5 and str(pin).isdigit() 