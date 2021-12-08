import os
import sys

import numpy as np

os.chdir("day_6")

lanternfish = []
with open("input.txt") as f:
    lanternfish = np.array([int(i) for i in f.readline().split(",")])

for i in range(80):
    lanternfish -= 1
    num_elapsed = np.where(lanternfish == -1)
    if len(num_elapsed[0]) > 0:
        lanternfish[num_elapsed] = 6
        lanternfish = np.append(lanternfish, [8 for i in range(len(num_elapsed[0]))])

result = len(lanternfish)


print(result)

