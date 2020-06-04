from itertools import zip_longest

def fold_array(arr, runs):
    """
    Fold an array Kata
    https://www.codewars.com/kata/57ea70aa5500adfe8a000110
    """
    for _ in range(runs):
        arr = [x+y for x,y in zip_longest(arr[:len(arr)//2], reversed(arr[len(arr)//2:]), fillvalue=0)]
    return arr