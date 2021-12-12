import os
import sys

from collections import deque

os.chdir("day_10")

with open("input.txt") as f:
    lines = f.readlines()

syntax_errors = 0
error_values = {")":3, "]":57, "}":1197, ">":25137}
open_close_pairs = {"(":")", "[":"]", "{":"}", "<":">"}

chunk_stack = deque()
for line in lines:
    for char in line.strip():
        if char in open_close_pairs.keys():
            chunk_stack.append(open_close_pairs[char])
        elif char in open_close_pairs.values():
            if char == chunk_stack[-1]:
                chunk_stack.pop()
            else:
                syntax_errors += error_values[char]
                break

print(syntax_errors)