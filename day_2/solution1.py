import os
import sys

os.chdir("day_2")

h_pos = 0
depth = 0

with open("input1.txt") as f:
    for line in f.readlines():
        command,value = line.split(" ")
        if command == "forward":
            h_pos += int(value)
        elif command == "down":
            depth += int(value)
        elif command == "up":
            depth -= int(value)
        if depth < 0: print("ich schwebe")

print(h_pos)
print(depth)
print(depth*h_pos)