import os
import sys
import numpy as np

os.chdir("day_3")


with open("input.txt") as f:
    lines = np.array([[int(char) for char in line.strip()] for line in f.readlines()])

oxy_candidates = lines
co2_candidates = lines
bit_counts = 0
for i in range(12):
    bit_counts_oxy = np.bincount(oxy_candidates.T[i])
    if bit_counts_oxy[0] == bit_counts_oxy[1]:
        cur_bit_oxy = 1
    else:
        cur_bit_oxy = bit_counts_oxy.argmax()
    oxy_candidates = oxy_candidates[np.where(oxy_candidates.T[i] == cur_bit_oxy)]
    if oxy_candidates.shape == (1,12): break

for i in range(12):
    bit_counts_co2 = np.bincount(co2_candidates.T[i])
    if bit_counts_co2[0] == bit_counts_co2[1]:
        cur_bit_co2 = 0
    else:
        cur_bit_co2 = bit_counts_co2.argmin()
    co2_candidates = co2_candidates[np.where(co2_candidates.T[i] == cur_bit_co2)]
    if co2_candidates.shape == (1,12): break



oxy_rating = int("".join([str(i) for i in oxy_candidates[0]]),2)
co2_rating = int("".join([str(i) for i in co2_candidates[0]]),2)
life_support = oxy_rating * co2_rating

print(oxy_rating)
print(co2_rating)
print(life_support)

