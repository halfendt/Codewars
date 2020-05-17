def is_triangle(a, b, c):
    """
    Is this a triangle? Kata
    https://www.codewars.com/kata/56606694ec01347ce800001b
    """
    p = (a+b+c)/2
    return (p*(p-a)*(p-b)*(p-c))**1/2 > 0
