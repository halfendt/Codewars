def better_than_average(class_points, your_points):
    """
    How good are you really? Kata
    https://www.codewars.com/kata/5601409514fc93442500010b
    """
    class_points.append(your_points)
    return your_points > sum(class_points)/len(class_points)