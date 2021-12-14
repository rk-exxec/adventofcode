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

for i in range(10):
    new_polymer = []
    for j in range(len(polymer)-1):
        pair = "".join(polymer[j:j+2])
        new_polymer.extend([polymer[j], rules[pair]])
    new_polymer.append(polymer[-1])
    polymer = new_polymer


#unique_elements = set(polymer)

#counts = [polymer.count(elem) for elem in unique_elements]
_,counts = np.unique(polymer, return_counts=True)

max_count = max(counts)
min_count = min(counts)

result = max_count - min_count

print(result)
