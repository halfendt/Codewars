import numpy as np

def solve_eq(eq):
    """
    Simultaneous Equations - Three Variables Kata
    https://www.codewars.com/kata/59280c056d6c5a74ca000149
    """
    eq_para = np.array(eq)[:,:3]
    eq_res = np.array(eq)[:,-1]
    return [int(x) for x in np.linalg.solve(eq_para, eq_res)]