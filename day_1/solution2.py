import os
import sys

os.chdir("./day_1")

num_incr = 0
sums = []
sum_check = []
sum_counter = 0
old_num = sys.maxsize
with open("./input1.txt",'r') as f:
    for line in f.readlines():
        new_num = int(line)

        sums.append(new_num)
        sum_check.append(1)
        if sum_counter >= 1: 
            sums[sum_counter - 1] += new_num
            sum_check[sum_counter - 1] += 1 
        if sum_counter >= 2: 
            sums[sum_counter - 2] += new_num
            sum_check[sum_counter - 2] += 1 
        sum_counter += 1


for sum_, chk_ in zip(sums,sum_check):
    if old_num < sum_ and chk_ == 3:
        num_incr += 1
    old_num = sum_

print(num_incr)