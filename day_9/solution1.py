import os
import sys

import numpy as np
from skimage.morphology import local_minima

os.chdir("day_9")


with open("input.txt") as f:
    lines = f.readlines()

height_map = np.array([[int(h) for h in line.strip()] for line in lines])

lowpoints = local_minima(height_map, connectivity=1, indices=True, allow_borders=True)

result = (height_map[lowpoints]+1).sum()

print(result)