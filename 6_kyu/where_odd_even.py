def iq_test(numbers):
    """
    IQ Test Kata
    https://www.codewars.com/kata/552c028c030765286c00007d
    """
    mod_list = [int(num)%2 for num in numbers.split()]
    return mod_list.index(1)+1 if sum(mod_list) == 1 else mod_list.index(0)+1