# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 14:49:29 2017

@author: oliver.cairns
"""

raw_data = "R2, L3, R2, R4, L2, L1, R2, R4, R1, L4, L5, R5, R5, R2, R2, R1, L2, L3, L2, L1, R3, L5, R187, R1, R4, L1, R5, L3, L4, R50, L4, R2, R70, L3, L2, R4, R3, R194, L3, L4, L4, L3, L4, R4, R5, L1, L5, L4, R1, L2, R4, L5, L3, R4, L5, L5, R5, R3, R5, L2, L4, R4, L1, R3, R1, L1, L2, R2, R2, L3, R3, R2, R5, R2, R5, L3, R2, L5, R1, R2, R2, L4, L5, L1, L4, R4, R3, R1, R2, L1, L2, R4, R5, L2, R3, L4, L5, L5, L4, R4, L2, R1, R1, L2, L3, L2, R2, L4, R3, R2, L1, L3, L2, L4, L4, R2, L3, L3, R2, L4, L3, R4, R3, L2, L1, L4, R4, R2, L4, L4, L5, L1, R2, L5, L2, L3, R2, L2"

# raw_data = "R2, L3"
# raw_data = "R2, R2, R2"
# raw_data = "R5, L5, R5, R3"

# North = 0, East = 1, South = 2, West = 3
current_orientation = 0
north_total = 0
east_total = 0
location_history = [[0, 0]]


def change_orientation(orientation, turning_instruction):
    if turning_instruction == "R":
        return (orientation + 1) % 4
    if turning_instruction == "L":
        return (orientation + 3) % 4


instructions = raw_data.split(", ")

# 1.a
for instruction in instructions:
    current_orientation = change_orientation(current_orientation, instruction[0])
    if current_orientation == 0:
        north_total += int(instruction[1:])
    if current_orientation == 1:
        east_total += int(instruction[1:])
    if current_orientation == 2:
        north_total -= int(instruction[1:])
    if current_orientation == 3:
        east_total -= int(instruction[1:])

print("1.a. distance", abs(north_total) + abs(east_total))

# 1.b - not yet working
current_orientation = 0
north_total = 0
east_total = 0
location_history = [[0, 0]]


i = -1
flag = True

while flag:
    i += 1
    instruction = instructions[i]
    current_orientation = change_orientation(current_orientation, instruction[0])
    if current_orientation == 0:
        north_total += int(instruction[1:])
    if current_orientation == 1:
        east_total += int(instruction[1:])
    if current_orientation == 2:
        north_total -= int(instruction[1:])
    if current_orientation == 3:
        east_total -= int(instruction[1:])
    if [north_total, east_total] in location_history:
        print("1.b. cross", abs(north_total) + abs(east_total))
        flag = False
    location_history.append([north_total, east_total])
