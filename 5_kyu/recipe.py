def cakes(recipe, available):
    """
    Pete, the baker Kata
    https://www.codewars.com/kata/525c65e51bf619685c000059
    """
    return min({k: available[k]//recipe[k] if k in available else 0 for k in recipe}.values())