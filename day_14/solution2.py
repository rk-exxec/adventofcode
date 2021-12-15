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
elem_counts = {key:0 for key in sorted(set(rules.values()))}
for char in polymer:
    elem_counts[char] += 1

# init counting table
for i in range(len(polymer)-1):
    pair_counts["".join(polymer[i:i+2])] += 1 

#new_counts = {k:v for k,v in pair_counts.items()}
 
for i in range(40):   
    new_counts = {k:v for k,v in pair_counts.items()}
    for k,v in pair_counts.items():
        if v == 0: continue
        insert = rules[k]
        new_1 = k[0] + insert
        new_2 = insert + k[1]
        new_counts[k] -= v
        new_counts[new_1] += v
        new_counts[new_2] += v
        
        elem_counts[insert] += v
    pair_counts = new_counts

max_count = max(elem_counts.values())
min_count = min(elem_counts.values())

result = max_count - min_count

print(result)
