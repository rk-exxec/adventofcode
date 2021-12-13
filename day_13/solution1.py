import os
import sys

import numpy as np
from matplotlib import pyplot as plt


os.chdir("day_13")


with open("input.txt") as f:
    lines = f.readlines()

sec_is_dots = True
folds = []
points = []
for line in lines:
    if line.strip() == "":
        sec_is_dots = False
        continue
    elif sec_is_dots:
        points.append([int(num) for num in line.strip().split(",")])
    else:
        ops = line.strip().split(" ")[-1].split("=")
        folds.append((ops[0], int(ops[1])))

points = np.array(points).T
dots = np.zeros((max(points[0])+1, max(points[1])+1), dtype=np.bool8)

dots[tuple(points)] = 1

def fold(a, axis, index):
    if axis == "x":
        rev_arr = np.flipud(a)
        a[:index,:] |= rev_arr[:index,:]
        return a[:index,:]
    else:
        rev_arr = np.fliplr(a)
        a[:,:index] |= rev_arr[:,:index]
        return a[:,:index]

result = fold(dots, *folds[0])

print(np.count_nonzero(result))

