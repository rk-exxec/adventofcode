import os
import sys

import numpy as np
from collections import deque

os.chdir("day_10")

with open("input.txt") as f:
    lines = f.readlines()

results = []
error_values = {")":1, "]":2, "}":3, ">":4}
open_close_pairs = {"(":")", "[":"]", "{":"}", "<":">"}
discard_line = False
chunk_stack = []
list_cntr = 0
for line in lines:
    
    chunk_stack.clear()
    for char in line.strip():
        if char in open_close_pairs.keys():
            chunk_stack.append(open_close_pairs[char])
        elif char in open_close_pairs.values():
            if char == chunk_stack[-1]:
                chunk_stack.pop()
            else:
                #syntax_errors += error_values[char]
                discard_line = True
                break
    if discard_line: 
        discard_line = False
        continue
    results.append(0)
    for symbol in reversed(chunk_stack):
        results[list_cntr] *= 5
        results[list_cntr] += error_values[symbol]
    list_cntr += 1

sorted_res = sorted(results)
result = sorted_res[len(sorted_res)//2]

print(result)