# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 10:07:33 2017

@author: oliver.cairns
"""
import csv

def count_jumps(instruction_list):
    i = 0
    jumps = 0
    while i > -1 and i < len(instruction_list):
        i_old = i
        i += instruction_list[i]
        instruction_list[i_old] += 1
        jumps +=1
        
    return jumps

def count_jumps_2(instruction_list):
    i = 0
    jumps = 0
    while i > -1 and i < len(instruction_list):
        i_old = i
        i += instruction_list[i]
        
        if instruction_list[i_old] > 2:
            instruction_list[i_old] -= 1
        else:
            instruction_list[i_old] += 1
        
        jumps +=1
        
    return jumps

data = []
with open('input_5.txt', newline='') as inputfile:
    for row in csv.reader(inputfile):
        data.append(row)

clean_data = [int(x[0]) for x in data]


assert count_jumps([0,3,0,1,-3]) == 5

assert count_jumps_2([0,3,0,1,-3]) == 10


print("1.a",count_jumps(clean_data))

clean_data = [int(x[0]) for x in data]

print("1.b",count_jumps_2(clean_data))
