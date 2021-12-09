import os
import sys

import numpy as np

os.chdir("day_8")

counter = 0
with open("input.txt") as f:
    for line in f.readlines():
        in_sig,out_sig = line.strip().split(" | ")
        out_segs = out_sig.split(" ")
        for seg in out_segs:
            if len(seg) in [2,4,3,7]:
                counter += 1

print(counter)