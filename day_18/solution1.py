
import os
import math
import numpy as np

os.chdir("day_18")

from snail_number import SnailNumber


with open("input.txt") as f:
    lines = f.readlines()

snail_numbers = []
for line in lines:
    snail_numbers.append(SnailNumber.load_from_text(line.strip()))

num: SnailNumber = None

for sn in snail_numbers:
    if num is None:
        num = sn
    else:
        num += sn
        #print(num)
        while(num.reduce()):
            pass

print(num.magnitude())