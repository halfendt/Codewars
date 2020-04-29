def people_with_age_drink(age):
    """
    Drink about Kata
    https://www.codewars.com/kata/56170e844da7c6f647000063
    """
    if age < 14:
        return 'drink toddy'
    elif age < 18:
        return 'drink coke'
    elif age < 21:
        return 'drink beer'
    else:
        return 'drink whisky'