import os
import sys

os.chdir("day_3")

gamma = 0
epsilon = 0
bit_counts = [0,0,0,0,0,0,0,0,0,0,0,0]
total_count = 0
with open("input.txt") as f:
    for line in f.readlines():
        for i in range(12):
            value = int(line, base=2)
            masked = value & (1 << i)
            if masked:
                bit_counts[i] += 1

        total_count += 1

threshold = total_count // 2
for i in range(12):
    if bit_counts[i] > threshold:
        gamma |= (1 << i)
    else:
        epsilon |= (1 << i)

print(gamma)
print(epsilon)
print(gamma*epsilon)

