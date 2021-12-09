import os
import sys

import numpy as np

os.chdir("day_7")

with open("input.txt") as f:
    data = np.array([int(i.strip()) for i in f.readline().split(",")])
# formula n*(n+1) / 2 fuel usage
old_fuel = 2**64 - 1
best_pos = 0
min_pos = min(data)
max_pos = max(data)
for i in range(min_pos, max_pos+1):
    distance = abs(data-i)
    fuel = (distance*(distance+1) // 2).sum()
    if fuel < old_fuel:
        old_fuel = fuel
        best_pos = i
        print(i)


result = old_fuel

print(result)