import os
import sys

import numpy as np

os.chdir("day_11")
grid = []
with open("input.txt") as f:
    grid = np.array([[char for char in line.strip()] for line in f.readlines()], dtype=np.int8)

num_flashes = 0
for i in range(100):
    grid += 1

    tempgrid = np.ma.array(grid)

    while(True):
        flashed = tempgrid > 9
        if not np.any(flashed): break
        tempgrid.mask |= tempgrid > 9
        for point in np.array(np.nonzero(flashed)).T:
            tempgrid[max(0,point[0]-1):min(99,point[0]+1)+1, max(0,point[1]-1):min(99,point[1]+1)+1] += 1
            num_flashes += 1
    
    grid[tempgrid.mask] = 0

print(num_flashes)