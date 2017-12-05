# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 18:50:16 2017

@author: oliver.cairns
"""

import csv

data = []
with open('input_5.txt', newline='') as inputfile:
    for row in csv.reader(inputfile):
        data.append(row)

def vowel_count(input_str):
    return len([x for x in input_str if x in ["a","e","i","o","u"]])

def double_char(input_str):
    flag = False
    for i in range(len(input_str)-1):
        if input_str[i] == input_str[i+1]:
            flag = True
    return flag

def no_failures(input_str):
    flag = True
    forbidden = ["ab", "cd", "pq", "xy"]
    for char in forbidden:
        if char in input_str:
            flag = False
    return flag

def one_gap_repeat(input_str):
    flag = False
    for i in range(len(input_str)-2):
        if input_str[i] == input_str[i+2]:
            flag = True
    return flag

def double_str_repeat(input_str):
    flag = False
    for i in range(len(input_str)-3):
        if input_str[i:i+2] in input_str[i+2:]:
            flag = True
    return flag


def is_nice(input_str):
    flag_1 = vowel_count(input_str) > 2
    flag_2 = double_char(input_str)
    flag_3 = no_failures(input_str)
    return flag_1 and flag_2 and flag_3

def is_nice_2(input_str):
    flag_1 = one_gap_repeat(input_str)
    flag_2 = double_str_repeat(input_str)
    return flag_1 and flag_2

assert is_nice("ugknbfddgicrmopn")

assert is_nice("aaa")

assert not is_nice("jchzalrnumimnmhp")

assert not is_nice("haegwjzuvuyypxyu")

assert not is_nice("dvszwmarrgswjxmb")

counter = 0
    
for string in data:
    if(is_nice(string[0])):
        counter +=1

print("1.a",counter)

assert is_nice_2("qjhvhtzxzqqjkmpb")

assert is_nice_2("xxyxx")

assert not is_nice_2("uurcxstgmygtbstg")

assert not is_nice_2("ieodomkazucvgmuy")


counter = 0
    
for string in data:
    if(is_nice_2(string[0])):
        counter +=1

print("1.b",counter)
