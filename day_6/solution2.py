import os
import sys

import numpy as np

from scipy.ndimage.interpolation import shift

os.chdir("day_6")

lanternfish = []
with open("input.txt") as f:
    lanternfish = np.array([int(i) for i in f.readline().split(",")], dtype=np.int8)

ages = np.bincount(lanternfish)
ages = np.append(ages, [0,0,0])
for i in range(256):
    print(i)
    temp = ages[0]
    ages = shift(ages, -1)
    ages[6] += temp
    ages[8] += temp

result = ages.sum()


print(result)

