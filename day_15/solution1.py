import os
import sys

import numpy as np

from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

os.chdir("day_15")

with open("input.txt") as f:
    lines = f.readlines()

risks = np.array([[int(char) for char in line.strip()] for line in lines], dtype=np.int8).T
risks2 = np.array([[int(char) for char in line.strip()] for line in lines], dtype=np.int8)
limits = risks.shape

grid = Grid(height=100, width=100, matrix=risks)

start = grid.node(0,0)
end = grid.node(99,99)

finder = AStarFinder()

path, runs = finder.find_path(start, end, grid)

print(grid.grid_str(path=path, start=start, end=end))

idx = np.array(path)

idx = tuple(idx.T)

weight = risks2[idx].sum() - risks[0,0]

print(len(path))

print(weight)