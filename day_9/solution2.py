import os
import sys

import numpy as np
from skimage.morphology import local_minima
from skimage.measure import label, regionprops, regionprops_table

os.chdir("day_9")


with open("input.txt") as f:
    lines = f.readlines()

height_map = np.array([[int(h) for h in line.strip()] for line in lines])

height_map = height_map < 9

label_im = label(height_map, connectivity=1)

props = regionprops(label_im,)


areas = sorted([prop["area"] for prop in props], reverse=True)

result = areas[0] * areas[1] * areas[2]


print(result)