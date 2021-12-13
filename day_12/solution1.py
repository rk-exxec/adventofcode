import os
import sys

import numpy as np
from collections import defaultdict
import copy

os.chdir("day_12")


with open("input.txt") as f:
    lines = f.readlines()

graph = defaultdict(set)

cur_path = []

for line in lines:
    node1, node2 = line.strip().split("-")
    graph[node1].add(node2)
    graph[node2].add(node1)

def possible_connections(start, cur_path, graph ):
    if start == "":
        start = "start"
    elif start == "end":
        return 1
    path = [node for node in cur_path]
    path.append(start)
    result = 0
    for node in graph[start]:
        if (node.islower() and not node in path) or node.isupper():
            result += possible_connections(node, path, graph)
    return result

result = possible_connections("start", [], graph)


print(result)