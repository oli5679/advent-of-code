# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 19:03:21 2017

@author: oliver.cairns
"""
from utils import import_txt_file


def find_distance(instructions):
    north = 0
    east = 0

    for instruction in instructions:
        if instruction == "n":
            north += 2
        if instruction == "ne":
            north += 1
            east += 1
        if instruction == "se":
            north -= 1
            east += 1
        if instruction == "s":
            north -= 2
        if instruction == "sw":
            north -= 1
            east -= 1
        if instruction == "nw":
            north += 1
            east -=1
    return(int((abs(north)+abs(east))/2))

def find_furthest_distance(instructions):
    north = 0
    east = 0
    furthest_distance = 0
    for instruction in instructions:
        if instruction == "n":
            north += 2
        if instruction == "ne":
            north += 1
            east += 1
        if instruction == "se":
            north -= 1
            east += 1
        if instruction == "s":
            north -= 2
        if instruction == "sw":
            north -= 1
            east -= 1
        if instruction == "nw":
            north += 1
            east -=1
        current_distance = int((abs(north)+abs(east))/2)
        if current_distance > furthest_distance:
            furthest_distance = current_distance
    return furthest_distance


        
assert(find_distance(["ne","ne","ne"]) == 3)
assert(find_distance(["ne","ne","sw","sw"]) == 0)
assert(find_distance(["ne","ne","s","s"]) == 2)
assert(find_distance(["se","sw","se","sw","sw"]) == 3)

raw_problem_data = import_txt_file("input_11.txt")
clean_problem_data = raw_problem_data[0].split(",")

print("11.a",find_distance(clean_problem_data))
print("11.b",find_furthest_distance(clean_problem_data))

