# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 14:14:31 2017

@author: oliver.cairns
"""

problem_data = [46,41,212,83,1,255,157,65,139,52,39,254,2,86,0,204]


def carry_out_instruction(index,instruction,string):
    #Rebase around the index
    rebased_string = string[index:] + string[:index]
    reversed_string = rebased_string[:instruction][::-1] + rebased_string[instruction:]
    final_string = reversed_string[index:] + reversed_string[:index]
    return final_string
 
assert carry_out_instruction(0,3,[0,1,2,3,4]) == [2, 1, 0, 3, 4]

print(carry_out_instruction(3,4,[2, 1, 0, 3, 4]))
    
