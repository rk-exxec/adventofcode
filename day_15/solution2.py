import os
import sys

import numpy as np

from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

os.chdir("day_15")

with open("input.txt") as f:
    lines = f.readlines()

risks = np.array([[int(char) for char in line.strip()] for line in lines], dtype=np.int8)

new_map = np.tile(risks, [5,5])

for i in range(5):
    for j in range(5):
        new_map[i*100:(i+1)*100, j*100:(j+1)*100] += i+j

new_map[np.where(new_map > 9)] -= 9

grid = Grid(height=500, width=500, matrix=new_map)

start = grid.node(0,0)
end = grid.node(499,499)

finder = AStarFinder()

path, runs = finder.find_path(start, end, grid)

idx = np.array(path)
idx = tuple(idx.T)

weight = new_map.T[idx].sum() - new_map[0,0]

print(len(path))
print(weight)