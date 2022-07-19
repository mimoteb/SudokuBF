from random import shuffle
from re import S
import numpy as np
import json
class sudoku:
        
    #                 first line            second line         3rd line
    #s = np.array([[00,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]])
    s = np.array([['l0c0','l0c1','l0c2','l0c3','l0c4','l0c5','l0c6','l0c7','l0c8'], \
        ['l1c0','l1c1','l1c2','l1c3','l1c4','l1c5','l1c6','l1c7','l1c8'], \
            ['l2c0','l2c1','l2c2','l2c3','l2c4','l2c5','l2c6','l2c7','l2c8'], \
            ['l3c0','l3c1','l3c2','l3c3','l3c4','l3c5','l3c6','l3c7','l3c8'], \
                ['l4c0','l4c1','l4c2','l4c3','l4c4','l4c5','l4c6','l4c7','l4c8'], \
                    ['l5c0','l5c1','l5c2','l5c3','l5c4','l5c5','l5c6','l5c7','l5c8'], \
                ['l6c0','l6c1','l6c2','l6c3','l6c4','l6c5','l6c6','l6c7','l6c8'], \
                    ['l7c0','l7c1','l7c2','l7c3','l7c4','l7c5','l7c6','l7c7','l7c8'], \
                        ['l8c0','l8c1','l8c2','l8c3','l8c4','l8c5','l8c6','l8c7','l8c8']])
    l0 = np.array(s[0])
    l1 = np.array(s[1])
    l2 = np.array(s[2])
    l3 = np.array(s[3])
    l4 = np.array(s[4])
    l5 = np.array(s[5])
    l6 = np.array(s[6])
    l7 = np.array(s[7])
    l8 = np.array(s[8])
    lines = [l0,l1,l2,l3,l4,l5,l6,l7,l8]

    c0 = np.array([l0[0], l1[0],l2[0],l3[0],l4[0],l5[0],l6[0],l7[0],l8[0]])
    c1 = np.array([l0[1],l1[1],l2[1],l3[1],l4[1],l5[1],l6[1],l7[1],l8[1]])
    c2 = np.array([l0[2],l1[2],l2[2],l3[2],l4[2],l5[2],l6[2],l7[2],l8[2]])
    c3 = np.array([l0[3],l1[3],l2[3],l3[3],l4[3],l5[3],l6[3],l7[3],l8[3]])
    c4 = np.array([l0[4],l1[4],l2[4],l3[4],l4[4],l5[4],l6[4],l7[4],l8[4]])
    c5 = np.array([l0[5],l1[5],l2[5],l3[5],l4[5],l5[5],l6[5],l7[5],l8[5]])
    c6 = np.array([l0[6],l1[6],l2[6],l3[6],l4[6],l5[6],l6[6],l7[6],l8[6]])
    c7 = np.array([l0[7],l1[7],l2[7],l3[7],l4[7],l5[7],l6[7],l7[7],l8[7]])
    c8 = np.array([l0[8],l1[8],l2[8],l3[8],l4[8],l5[8],l6[8],l7[8],l8[8]])
    columns =[c0,c1,c2,c3,c4,c5,c6,c7,c8]

    b0 = np.array([s[0,0], s[0,1], s[0,2], s[1,0], s[1,1],s[1,2], s[2,0], s[2,1], s[2,2]])
    b1 =  np.array([s[0,3], s[0,4], s[0,5], s[1,3], s[1,4],s[1,5], s[2,3], s[2,4], s[2,5]])
    b2 = np.array([s[0,6], s[0,7], s[0,8], s[1,6], s[1,7],s[1,8], s[2,6], s[2,7], s[2,8]])
    b3 = np.array([s[3,0], s[3,1], s[3,2], s[4,0], s[4,1],s[4,2], s[5,0], s[5,1], s[5,2]])
    b4 = np.array([s[3,3], s[3,4], s[3,5], s[4,3], s[4,4],s[4,5], s[5,3], s[5,4], s[5,5]])
    b5 = np.array([s[3,6], s[3,7], s[3,8], s[4,6], s[4,7],s[4,8], s[5,6], s[5,7], s[5,8]])
    b6 = np.array([s[6,0], s[6,1], s[6,2], s[7,0], s[7,1],s[7,2], s[8,0], s[8,1], s[8,2]])
    b7 = np.array([s[6,3], s[6,4], s[6,5], s[7,3], s[7,4],s[7,5], s[8,3], s[8,4], s[8,5]])
    b8 = np.array([s[6,6], s[6,7], s[6,8], s[7,6], s[7,7],s[7,8], s[8,6], s[8,7], s[8,8]])
    blocks = [b0, b1, b2, b3, b4, b5, b6, b7, b8]
    #zerofying sudoku
    #for i in s:
    #    s[i]=0
    grid = [[0 for i in range(9)] for j in range(9)]
    j = json.dumps(s.tolist())
    with open('sudoku.json','w') as w:
        w.write(j)
    print(j)
sk = sudoku()

def generate_sudoku(mask_rate=0.5):
    while True:
        n = 9
        m = np.zeros((n, n), np.int)
        rg = np.arange(1, n + 1)
        m[0, :] = np.random.choice(rg, n, replace=False)
        try:
            for r in range(1, n):
                for c in range(n):
                    col_rest = np.setdiff1d(rg, m[:r, c])
                    row_rest = np.setdiff1d(rg, m[r, :c])
                    avb1 = np.intersect1d(col_rest, row_rest)
                    sub_r, sub_c = r//3, c//3
                    avb2 = np.setdiff1d(np.arange(0, n+1), m[sub_r*3:(sub_r+1)*3, sub_c*3:(sub_c+1)*3].ravel())
                    avb = np.intersect1d(avb1, avb2)
                    m[r, c] = np.random.choice(avb, size=1)
            break
        except ValueError:
            pass
    print("Answer:\n", m)
    mm = m.copy()
    mm[np.random.choice([True, False], size=m.shape, p=[mask_rate, 1 - mask_rate])] = 0
    print("\nMasked anwser:\n", mm)
    np.savetxt("./puzzle.csv", mm, "%d", delimiter=",")
    return mm


def solve(m):
    if isinstance(m, list):
        m = np.array(m)
    elif isinstance(m, str):
        m = np.loadtxt(m, dtype=np.int, delimiter=",")
    rg = np.arange(m.shape[0]+1)
    while True:
        mt = m.copy()
        while True:
            d = []
            d_len = []
            for i in range(m.shape[0]):
                for j in range(m.shape[1]):
                    if mt[i, j] == 0:
                        possibles = np.setdiff1d(rg, np.union1d(np.union1d(mt[i, :], mt[:, j]), mt[3*(i//3):3*(i//3+1), 3*(j//3):3*(j//3+1)]))
                        d.append([i, j, possibles])
                        d_len.append(len(possibles))
            if len(d) == 0:
                break
            idx = np.argmin(d_len)
            i, j, p = d[idx]
            if len(p) > 0:
                num = np.random.choice(p)
            else:
                break
            mt[i, j] = num
            if len(d) == 0:
                break
        if np.all(mt != 0):
            break

    print("\nTrail:\n", mt)
    return mt


def check_solution(m):
    if isinstance(m, list):
        m = np.array(m)
    elif isinstance(m, str):
        m = np.loadtxt(m, dtype=np.int, delimiter=",")
    set_rg = set(np.arange(1, m.shape[0] + 1))
    no_good = False
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            r1 = set(m[3 * (i // 3):3 * (i // 3 + 1), 3 * (j // 3):3 * (j // 3 + 1)].ravel()) == set_rg
            r2 = set(m[i, :]) == set_rg
            r3 = set(m[:, j]) == set_rg
            if not (r1 and r2 and r3):
                no_good = True
                break
        if no_good:
            break
    if no_good:
        print("\nChecked: not good")
    else:
        print("\nChecked: OK")


if __name__ == "__main__":
    puzzle = generate_sudoku(mask_rate=0.7)
    solved = solve(puzzle)
    check_solution(solved)
