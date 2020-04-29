from math import pi, log

def converter(n, decimals=0, base=pi):
    """
    Decimal to any Rational or Irrational Base Converter Kata
    https://www.codewars.com/kata/5509609d1dbf20a324000714
    """
    alpha = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if n == 0: return '0' if not decimals else '0.' + '0'*decimals

    result = '' if n > 0 else '-'
    n = abs(n)

    for i in range(int(log(n, base)), -decimals-1, -1):
        if i == -1: 
            result += '.'
        result +=  alpha[int(n / base**i)]
        n %= base**i
    return result