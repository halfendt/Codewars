def dirReduc(arr):
    """
    Directions Reduction Kata
    https://www.codewars.com/kata/550f22f4d758534c1100025a
    """
    dir_dict = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    res = []
    for direc in arr:
        if res and dir_dict[direc] == res[-1]:
            res.pop()
        else:
            res.append(direc)
    return res