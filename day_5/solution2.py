import os
import sys

import numpy as np

os.chdir("day_5")

start_points = []
end_points = []
with open("input.txt") as f:
    for line in f.readlines():
        pairs = line.split("->")
        x1,y1 = [int(i.strip()) for i in pairs[0].split(",")]
        x2,y2 = [int(i.strip()) for i in pairs[1].split(",")]
        start_points.append([x1,y1])
        end_points.append([x2,y2])

max_y = 1000
max_x = 1000

plane = np.zeros((max_x,max_y), dtype=np.int16)

for s,e in zip(start_points, end_points):
    if s[0] == e[0]: # horizontals
        if s[1] < e[1]:
            plane[s[0],s[1]:e[1]+1] += 1
        else:
            plane[s[0],e[1]:s[1]+1] += 1
    elif s[1] == e[1]: # verticals
        if s[0] < e[0]:
            plane[s[0]:e[0]+1,s[1]] += 1
        else:
            plane[e[0]:s[0]+1,s[1]] += 1
    else: # diagonals
        if(s[0] > e[0]):
            rangex = range(s[0],e[0]-1,-1)
        else:
            rangex = range(s[0],e[0]+1)
        
        if(s[1] > e[1]):
            rangey = range(s[1],e[1]-1,-1)
        else:
            rangey = range(s[1],e[1]+1)
        plane[rangex,rangey] += 1


locations = plane[np.where(plane >= 2)]
result = len(locations)

print(result)