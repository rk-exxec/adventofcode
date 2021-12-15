import os
import sys

import numpy as np

os.chdir("day_14")

with open("input.txt") as f:
    lines = f.readlines()

polymer = [char for char in lines[0].strip()]

rules = {}

for line in lines[2:]:
    pair, insert = line.strip().split(" -> ")
    rules[pair] = insert

for i in range(3):
    new_polymer = []
    for j in range(len(polymer)-1):
        pair = "".join(polymer[j:j+2])
        new_polymer.extend([polymer[j], rules[pair]])
    new_polymer.append(polymer[-1])
    polymer = new_polymer

items,counts = np.unique(polymer, return_counts=True)

elems = {i:c for i,c in zip(items,counts)}

print(elems)

max_count = max(counts)
min_count = min(counts)

result = max_count - min_count

print(result)
