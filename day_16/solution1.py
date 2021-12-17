import os
import sys

import numpy as np
import binascii

os.chdir("day_16")

with open("input.txt") as f:
    line = f.readline().strip()

def parse_operator(bits):
    op_type = bits[0]
    data = bits[1:]
    value = 0
    version = 0
    if op_type == "1": # num of packets
        num_packets = int(data[:11],2)
        start = 11
        for _ in range(num_packets):
            val, ver, idx = decode_packet(data[start:])
            start += idx
            value += val
            version += ver
        idx = start

    else: # num of bits
        num_bits = int(data[:15],2)
        val, ver, _ = decode_packet(data[15:15+num_bits+1])
        value += val
        version += ver
        idx = 15 + num_bits + 1
    return version, value, idx

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
    if len(bin_string) < 6:
        return 0,0,0
    version = int(bin_string[0:3],2)
    packet_type = bin_string[3:6]
    value = 0
    
    if packet_type == "100": # literal value
        value, idx = parse_literal(bin_string[6:])
        idx += 6

    else: # operator
        ver, value, idx = parse_operator(bin_string[6:])
        version += ver
        idx += 6
    print(value, version, idx)
    return value, version, idx

bin_string = f"{int(line,16):0>b}"

val, ver, idx = decode_packet(bin_string)

print(val)
print(ver)
