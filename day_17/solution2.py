import os
import sys

import numpy as np
from matplotlib import pyplot as plt

os.chdir("day_17")

with open("input.txt") as f:
    line = f.readline().strip()

values = line.split(":")[1].split(",")

x1, x2 = [int(x) for x in values[0].split("=")[1].split("..")]

y1, y2 = [int(y) for y in values[1].split("=")[1].split("..")]


def xstep(pos, vel):
    new_pos = pos + vel
    if vel == 0:
        xf = 0
    elif vel < 0:
        xf = 1
    else: 
        xf = -1

    new_vel = vel + xf
    return new_pos, new_vel

def ystep(pos, vel):
    new_pos = pos + vel

    new_vel = vel - 1
    return new_pos, new_vel

def ycheck(pos, target):
    y1,y2 = target
    if y1 <= pos <= y2:
        return 1
    elif pos > y2:
        return 0
    elif pos < y1:
        return 2

def xcheck(pos, target):
    x1,x2 = target
    if x1 <= pos <= x2:
        return 1
    elif pos < x1:
        return 0
    elif pos > x2:
        return 2

y_range = range(-200,200)

x_range = range(0,200)

hits = np.zeros((x2-x1+1, y2-y1+1), dtype=np.int32)
candidates = []
for ivelx in x_range:
    for ively in y_range:
        posx = 0
        posy = 0
        velx = ivelx
        vely = ively
        #print(velx,vely)
        while True:
            posx, velx = xstep(posx, velx)
            posy, vely = ystep(posy, vely)
            if xcheck(posx,(x1,x2)) == 1 and ycheck(posy,(y1,y2)) == 1:
                candidates.append((ivelx, ively))
                hits[posx-x1,posy-y1] += 1
                break
            elif xcheck(posx,(x1,x2)) == 2 or ycheck(posy,(y1,y2)) == 2:
                break

plt.imshow(hits.T, cmap='hot')
plt.show()
print(candidates)
print(hits.sum())