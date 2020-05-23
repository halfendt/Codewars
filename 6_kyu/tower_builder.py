def tower_builder(n_floors):
    """
    Build Tower Kata
    https://www.codewars.com/kata/576757b1df89ecf5bd00073b
    """
    return[' '*(n_f-1)+'*'*((2*n_floors-1)-(n_f-1)*2)+' '*(n_f-1) for n_f in range(1, n_floors+1)][::-1]