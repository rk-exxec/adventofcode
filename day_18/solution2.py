import os
import math
import copy
import numpy as np

os.chdir("day_18")

from snail_number import SnailNumber


with open("input.txt") as f:
    lines = f.readlines()

snail_numbers = []
for line in lines:
    snail_numbers.append(SnailNumber.load_from_text(line.strip()))

num: SnailNumber = None
max_magnitude = 0

for i in range(len(snail_numbers)):
    for j in range(len(snail_numbers)):
        if i==j: continue
        num = copy.deepcopy(snail_numbers[i]) + copy.deepcopy(snail_numbers[j])

        while(num.reduce()):
            pass
        magn = num.magnitude()
        print(i, ".", j, ": ", magn)
        if magn > max_magnitude:
            max_magnitude = magn

print(max_magnitude)