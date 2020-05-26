def snail(snail_map):
    """
    Snail Kata
    https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1
    """
    res_list = []
    while len(snail_map) > 0:
        res_list.extend(snail_map[0])
        snail_map.pop(0)
        for i in range(len(snail_map)):
            res_list.append(snail_map[i][-1])
            snail_map[i].pop(-1)
        if len(snail_map) > 0:
            res_list.extend(snail_map[-1][::-1])
            snail_map.pop(-1)
        for i in reversed(range(len(snail_map))):
            res_list.append(snail_map[i][0])
            snail_map[i].pop(0)
    return res_list