import os
import sys

os.chdir("./day_1")

num_incr = 0
old_num = sys.maxsize
with open("./input1.txt",'r') as f:
    for line in f.readlines():
        new_num = int(line)
        if old_num < new_num:
            num_incr += 1
        old_num = new_num

print(num_incr)