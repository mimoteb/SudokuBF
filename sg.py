import json
from random import sample
from math import sqrt

import numpy
import numpy as np

def Sudoku():
    size = 9
    len = int(sqrt(size))
    cells = list(range(len))

    rows  = [x*len+w for x in sample(cells, len) for w in sample(cells, len)]
    cols  = [y*len+h for y in sample(cells, len) for h in sample(cells, len)]
    nums = sample(list(range(1, size+1)), size)

    def pattern(x, y):
        return (x + y//len + len*(y%len))%size

    board = [[nums[pattern(row, col)] for col in cols] for row in rows]

    squares = size*size
    empties = int(squares * 0.6)

    for square in sample(range(squares), empties):
        board[square//size][square%size] = 0

    return board

# print("\nSudoku creator for different size variants such as: \n")
# for i in range(2, 11):
#     print(i*i, "x", i*i)
size = 9
board = Sudoku()
print("\nSudoku sudoku.json created:\n")
with open('sudoku.json', 'w') as w:
    w.write(json.dumps(board))
w.close()
def solve(sudokuJson):
    if isinstance(sudokuJson, list):
        sudokuJson = np.array(sudokuJson)
    elif isinstance(sudokuJson, str):
        sudokuJson = np.loadtxt(sudokuJson, dtype=int, delimiter=",")
    rg = np.arange(sudokuJson.shape[0]+1)
    while True:
        mt = sudokuJson.copy()
        while True:
            d = []
            d_len = []
            for i in range(sudokuJson.shape[0]):
                for j in range(sudokuJson.shape[1]):
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

with open('sudoku.json','r') as r:
    sjson = r.readline()
r.close()
print(r)
#solve(sjson)
