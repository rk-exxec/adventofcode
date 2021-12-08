import os
import sys

import numpy as np

os.chdir("day_4")

with open("input.txt") as f:
    lines = f.readlines()

draw_numbers = []
boards = []
cur_board_cntr = 0
draw_numbers = [int(i) for i in lines[0].strip().split(",")]
rows = []
for i in range(2, len(lines)):
    if lines[i] == "\n":
        boards.append(np.array(rows))
        rows.clear()
        cur_board_cntr += 1
    else:
        row = [int(l.strip()) for l in lines[i].strip().split(" ") if l != ""]
        rows.append(row)

boards = np.array(boards)
marked_boards = np.zeros_like(boards, dtype=np.bool8)

for num in draw_numbers:
    marked_boards[np.where(boards == num)] = True
    bingo = False
    for i in range(marked_boards.shape[0]):
        for j in range(5):
            bingo |= marked_boards[i][j].all() or marked_boards[i].T[j].all()
        
        if bingo:
            print(i)
            sum_of_unmarked = boards[i][np.where(marked_boards[i] != True)].sum()
            result = sum_of_unmarked * num
            break
    if bingo:
        break


print(result)
