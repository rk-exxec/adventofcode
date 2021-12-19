import os
import sys

import numpy as np
import binascii
import math

os.chdir("day_16")

with open("input.txt") as f:
    line = f.readline().strip()

def parse_operator(bits, op):
    op_type = bits[0]
    data = bits[1:]
    values = []
    if op_type == "1": # num of packets
        num_packets = int(data[0:11],2)
        start = 11
        for _ in range(num_packets):
            val, idx = decode_packet(data[start:])
            start += idx
            values.append(val)
        idx = start 

    else: # num of bits
        num_bits = int(data[0:15],2)
        data = data[15:]
        idx = 0
        while(True):
            val, i = decode_packet(data[idx:])
            idx += i
            values.append(val)
            if idx == num_bits: break
        idx += 15

    value = apply_operator(values, op)
    return value, idx + 1

def apply_operator(values, op):
    if op == 0:
        return sum(values)
    elif op == 1:
        return math.prod(values)
    elif op == 2:
        return min(values)
    elif op == 3:
        return max(values)
    elif op == 5:
        return int(values[0] > values[1])
    elif op == 6:
        return int(values[0] < values[1])
    elif op == 7:
        return int(values[0] == values[1])
    else:
        print("invalid operator")
        return 0

def parse_literal(bits):
    i = 0
    nums = []
    while(bits[5*i] == "1"):
        literal = bits[1+5*i:5+5*i]
        i += 1
        nums.append(literal)

    literal = bits[1+5*i:5+5*i]
    idx = 5+5*i
    nums.append(literal)

    number = "".join(nums)
    value = int(number,2)
    return value, idx

def decode_packet(bin_string):
    version = int(bin_string[0:3],2)
    packet_type = int(bin_string[3:6],2)
    value = 0
    if packet_type == 4: # literal value
        value, idx = parse_literal(bin_string[6:])
        idx += 6

    else: # operator
        value, idx = parse_operator(bin_string[6:], packet_type)
        idx += 6

    return value, idx

bin_string = bin(int(line,16))[2:].zfill(len(line*4))

val, idx = decode_packet(bin_string)

print(val)
