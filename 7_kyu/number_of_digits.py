def nb_dig(n, d):
    """
    Count the Digit Kata
    https://www.codewars.com/kata/566fc12495810954b1000030
    """
    return ''.join(str(num**2) for num in range(n+1)).count(str(d))