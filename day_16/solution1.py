import os
import sys

import numpy as np
import binascii

os.chdir("day_16")

with open("input.txt") as f:
    line = f.readline().strip()


def decode_packet(bin_string):
    if len(bin_string) < 6:
        return 0,0,0
    version = int(bin_string[0:3],2)
    packet_type = bin_string[3:6]
    value = 0
    
    if packet_type == "100": # literal value
        i = 0
        nums = []
        while(bin_string[6+5*i] == "1"):
            i += 1
            literal = bin_string[7+5*i:11+5*i]
            nums.append(str(int(literal,2)))

        literal = bin_string[7+5*i:11+5*i]
        idx = 11+5*i+1
        #idx = idx + (4 - idx % 4)
        nums.append(str(int(literal,2)))
        value = int("".join(nums))

    else: # operator
        if bin_string[6] == "1": # num of packets
            num_packets = int(bin_string[7:18],2)
            start = 18
            for i in range(num_packets):
                val, ver, idx = decode_packet(bin_string[start:])
                start += idx + 1
                value += val
                version += ver
            idx = start 

        else: # num of bits
            num_bits = int(bin_string[7:22],2)
            val, ver, _ = decode_packet(bin_string[22:22+num_bits+1])
            value += val
            version += ver
            idx = 22 + num_bits + 1
    print(value, version, idx)
    return value, version, idx

bin_string = f"{int(line,16):0>b}"

val, ver, idx = decode_packet(bin_string)

print(val)
print(ver)
