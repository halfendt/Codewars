def sum_dif_rev(n):
    """
    Sum and Rest the Number with its Reversed and See What Happens
    https://www.codewars.com/kata/5603a9585480c94bd5000073/solutions/python
    """
    num_list = []
    for num in range(9, 1000000, 9):
        try:
            if int(str(num)[-1]) == 0:
                pass
            elif (num + int(str(num)[::-1])) % abs(num - int(str(num)[::-1])) == 0:
                num_list.append(num)
        except:
            pass
    return num_list[n-1]