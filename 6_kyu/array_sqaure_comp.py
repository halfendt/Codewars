def comp(array1, array2):
    """
    Are they the "same"? Kata
    https://www.codewars.com/kata/550498447451fbbd7600041c
    """
    try:
        return sorted([i**2 for i in array1]) == sorted(array2)
    except:
        return False