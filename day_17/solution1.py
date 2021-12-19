import os
import sys

import numpy as np

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

def check(pos, target):
    xp,yp = pos
    x1,y1,x2,y2 = target

    if x1 <= xp <= x2 and y1 <= yp <= y2:
        return 1 # hit target
    elif xp < x2 and yp > y1:
        return 2 # not hit but can still hit
    else:
        return 0 # cannot hit anymore

def ycheck(pos, target):
    y1,y2 = target
    if y1 <= pos <= y2:
        return 1
    elif pos > y2:
        return 0
    elif pos < y1:
        return 2

def xcheck(pos, target, vel):
    x1,x2 = target
    if vel == 0:
        return 2
    elif x1 <= pos <= x2:
        return 1
    elif pos < x1:
        return 0
    elif pos > x2:
        return 2


y_range = range(-100,200)

max_pos = 0

for i in y_range:
    vel = i
    pos = 0
    cur_max_pos = 0
    while True:
        pos, vel = ystep(pos, vel)
        if cur_max_pos < pos: 
            cur_max_pos = pos
        if ycheck(pos,(y1,y2)) == 1:
            if max_pos < cur_max_pos:
                max_pos = cur_max_pos
            break
        elif ycheck(pos,(y1,y2)) == 2:
            break

print (max_pos)