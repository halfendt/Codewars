import numpy as np

def youre_winner(pieces_position_list):
    """
    Connect Four Kata
    https://www.codewars.com/kata/56882731514ec3ec3d000009
    """
    conn_four = np.full((6,7),' ')
    moves = [move.split('_') for move in pieces_position_list]
    num_A = 0
    num_B = 0
    num_C = 0
    num_D = 0
    num_E = 0
    num_F = 0
    num_G = 0
    for m in moves:
        if m[0] == 'A':
            conn_four[-1-num_A][0] = m[1][0]
            num_A += 1
        elif m[0] == 'B':
            conn_four[-1-num_B][1] = m[1][0]
            num_B += 1
        elif m[0] == 'C':
            conn_four[-1-num_C][2] = m[1][0]
            num_C += 1
        elif m[0] == 'D':
            conn_four[-1-num_D][3] = m[1][0]
            num_D += 1
        elif m[0] == 'E':
            conn_four[-1-num_E][4] = m[1][0]
            num_E += 1
        elif m[0] == 'F':
            conn_four[-1-num_F][5] = m[1][0]
            num_F += 1
        elif m[0] == 'G':
            conn_four[-1-num_G][6] = m[1][0]
            num_G += 1

        # Check for four in diagonal
        diags = [conn_four[::-1,:].diagonal(i).tolist() for i in range(-conn_four.shape[0]+1, conn_four.shape[1])]
        diags.extend(conn_four.diagonal(i).tolist() for i in range(conn_four.shape[1]-1, -conn_four.shape[0], -1))
        for d in [n for n in diags if len(n)>=4]:
            if list_in(['Y']*4, d):
                return 'Yellow'
            elif list_in(['R']*4, d):
                return 'Red'

        # Check for four in row
        #row = [row[0+i:4+i] for row in conn_four[::-1,:].tolist() for i in range(4)]
        for row in conn_four[::-1,:].tolist():
            if list_in(['Y']*4, row):
                return 'Yellow'
            elif list_in(['R']*4, row):
                return 'Red'

        # Check for four in column
        #col = [row[0+i:4+i] for row in conn_four[::-1,:].T.tolist() for i in range(3)]
        for col in conn_four[::-1,:].T.tolist():
            if list_in(['Y']*4, col):
                return 'Yellow'
            elif list_in(['R']*4, col):
                return 'Red'
    return 'Draw'

def list_in(a, b):
    return any(map(lambda x: b[x:x + len(a)] == a, range(len(b) - len(a) + 1)))
