import os
import sys
from types import coroutine

import numpy as np

os.chdir("day_8")

def get_difference(a, b):
    set1 = set(a)
    set2 = set(b)
    return list(set1.symmetric_difference(set2))

def get_common(a,b):
    return list(set(a)&set(b))

def find_segs_contains(a:str,b:list):
    for segs in b:
        contains = True
        for char in a:
            if not char in segs:
                contains &= False
        if contains:
            return segs

def analyze_input(signals):
    in_segs = signals.split(" ")
    one = ""
    four = ""
    seven = ""
    eight = ""
    seg235 = []
    seg690 = []
    for seg in in_segs:
        if len(seg) == 2: one = seg
        elif len(seg) == 4: four = seg
        elif len(seg) == 3: seven = seg
        elif len(seg) == 7: eight = seg
        elif len(seg) == 5: seg235.append(seg)
        elif len(seg) == 6: seg690.append(seg)
    # direction: top top-left top-right middle bot-left bot-right bottom
    top = get_difference(one, seven)[0]
    mid_tleft = get_difference(one, four)
    bleft_bot = get_difference(four,eight) # yields top, bleft, bot
    bleft_bot.remove(top) # remove top
    three = find_segs_contains(one, seg235) # find the three, only 5 seg number that contains the 1 segments
    bot = get_common(three, bleft_bot)[0]
    mid = get_common(mid_tleft, three)[0]
    tleft = get_difference(mid, mid_tleft)[0]
    bleft = get_difference(bot, bleft_bot)[0]
    five = find_segs_contains(tleft, seg235)
    bright = get_common(one, five)[0]
    tright = get_difference(one ,bright)[0]

    return top, tleft, tright, mid, bleft, bright, bot


def build_decoder_sets(code) -> list[set]:
    sets = []
    zero = [0,1,2,4,5,6]
    one = [2,5]
    two = [0,2,3,4,6]
    three = [0,2,3,5,6]
    four = [1,2,3,5]
    five = [0,1,3,5,6]
    six = [0,1,3,4,5,6]
    seven = [0,2,5]
    eight = [0,1,2,3,4,5,6]
    nine = [0,1,2,3,5,6]
    numbers = [zero, one, two ,three, four, five, six, seven, eight, nine]
    for num in numbers:
        sets.append(set([code[idx] for idx in num]))

    return sets


def decode(digits, code):
    result = []
    # building sets:
    decoder_sets = build_decoder_sets(code)
    for digit in digits:
        d = set(digit)
        for i,s in enumerate(decoder_sets):
            if len(s.symmetric_difference(d)) == 0:
                result.append(i)
                break

    return int(''.join(map(str,result)))


        
result = 0
with open("input.txt") as f:

    for line in f.readlines():
        in_sig,out_sig = line.strip().split(" | ")
        code = analyze_input(in_sig)
        number = decode(out_sig.split(" "), code)
        result += number
        print(number)

print(result)