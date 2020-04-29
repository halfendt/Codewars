def next_bigger(n):
    """
    Next bigger number with the same digits Kata
    https://www.codewars.com/kata/55983863da40caa2c900004e
    """
    list_ints=list(map(int,str(n)))
    for ind in reversed(range(len(list_ints))):
        if ind == 0:
            return -1
        if list_ints[ind] > list_ints[ind-1]:
            break
    left, right=list_ints[:ind], list_ints[ind:]
    for knd in reversed(range(len(right))):
        if right[knd] > left[-1]:
            right[knd], left[-1] = left[-1], right[knd]
            break
    return int("".join(map(str, (left + sorted(right)))))