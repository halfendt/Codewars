from math import cos, sin, pi

def crusoe(n, d, ang, dist_mult, ang_mult):
    """
    Robinson Crusoe Kata
    https://www.codewars.com/kata/5d95b7644a336600271f52ba
    """
    ang *= pi/180
    x = d*cos(ang)
    y = d*sin(ang)
    for _ in range(n-1):
        d *= dist_mult
        ang *= ang_mult
        x += d*cos(ang)
        y += d*sin(ang)
    return x, y