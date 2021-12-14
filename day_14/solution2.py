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

pair_counts = {key:0 for key in rules.keys()}
elem_counts = {key:0 for key in set(rules.values())}
for char in polymer:
    elem_counts[char] += 1

# init counting table
for i in range(len(polymer)-1):
    pair_counts["".join(polymer[i:i+2])] += 1 

#new_counts = {k:v for k,v in pair_counts.items()}
 
for i in range(40):   
    new_counts = {k:0 for k in pair_counts.keys()}
    for k,v in pair_counts.items():
        if v == 0: continue
        insert = rules[k]
        new_counts[k[0]+insert] = pair_counts[k[0]+insert] + 1
        new_counts[insert + k[1]] = pair_counts[insert + k[1]] + 1
        elem_counts[insert] += 1
    pair_counts = new_counts


max_count = max(elem_counts.values())
min_count = min(elem_counts.values())

result = max_count - min_count

print(result)
