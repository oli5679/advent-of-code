# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 12:56:53 2017

@author: oliver.cairns
"""
import copy

def find_largest_index(blocks):
    max_value = max(blocks)
    max_index = blocks.index(max_value)
    return max_index

def reallocation_cycle(blocks):
    target = find_largest_index(blocks)
    target_len = blocks[target]
    blocks[target] = 0
    for i in range(target_len):
        add_index = (target + i + 1) % len(blocks)
        blocks[add_index] += 1
    
    return blocks

assert(reallocation_cycle([0, 2, 7, 0])) ==  [2, 4, 1, 2]

assert(reallocation_cycle( [2, 4, 1, 2])) == [3, 1, 2, 3]

assert(reallocation_cycle(  [3, 1, 2, 3])) == [0, 2, 3, 4]

#6.a
blocks = [10, 3,	15, 10, 5,	15,	5, 15, 9,	2,	5,	8,	5,	2,	3,	6]


history = [copy.copy(blocks)]
flag = True
i = 0

while flag:
    i += 1
    blocks = reallocation_cycle(blocks)
    if blocks in history:
        flag = False
        print("6.a",i)
        print("6.b",i - history.index(blocks))
    history.append(copy.copy(blocks))