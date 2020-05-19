def sum_dig_pow(a, b):
    """
    Take a Number And Sum Its Digits Raised To The Consecutive Powers And ....¡Eureka!! Kata
    https://www.codewars.com/kata/5626b561280a42ecc50000d1
    """
    return [num for num in range(a, b+1) if sum(int(dig)**exp for exp, dig in enumerate(str(num), 1)) == num]