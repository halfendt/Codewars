def move_zeros(array):
    """
    Moving Zeros To The End Kata
    https://www.codewars.com/kata/52597aa56021e91c93000cb0
    """
    new_list = []
    zeros_list = []
    for ele in array:
        if ele == 0 and type(ele) != bool:
            zeros_list.append(ele)
        else:
            new_list.append(ele)
    new_list.extend(zeros_list)
    return new_list