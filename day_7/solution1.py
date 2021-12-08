import os
import sys

import numpy as np

os.chdir("day_7")

with open("input.txt") as f:
    data = np.array([int(i.strip()) for i in f.readline().split(",")])

position = np.median(data)

result = np.abs(data - position).sum()

print(result)