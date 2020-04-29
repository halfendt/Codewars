from collections import Counter
import numpy as np

def find_uniq(arr):
    """
    Find the unique number Kata
    https://www.codewars.com/kata/585d7d5adb20cf33cb000235
    """
    my_map = dict(Counter(np.array(arr)))
    return dict(zip(my_map.values(), my_map.keys()))[1]