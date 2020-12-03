# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 11:06:58 2017

@author: oliver.cairns
"""
import csv


def is_valid(str):
    flag = True
    word_list = str.split(" ")
    for char in word_list:
        if word_list.count(char) > 1:
            flag = False
    return flag


def is_valid_2(str):
    flag = True
    word_list = str.split(" ")
    sorted_word_list = [sorted(word) for word in word_list]
    for char in sorted_word_list:
        if sorted_word_list.count(char) > 1:
            flag = False
    return flag


assert is_valid("aa bb cc dd ee")

assert not is_valid("aa bb cc dd aa")

assert is_valid("aa bb cc dd aaa")

data = []
with open("input_4.txt", newline="") as inputfile:
    for row in csv.reader(inputfile):
        data.append(row)

counter = 0

for row in data:
    if is_valid(row[0]):
        counter += 1
print("4.a", counter)

assert is_valid_2("abcde fghij")
assert not is_valid_2("abcde xyz ecdab")
assert is_valid_2("a ab abc abd abf abj")
assert is_valid_2("iiii oiii ooii oooi oooo")

counter_2 = 0

for row in data:
    if is_valid_2(row[0]):
        counter_2 += 1

print("4.b", counter_2)
