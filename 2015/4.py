# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 17:59:06 2017

@author: oliver.cairns
"""
import hashlib

input_str = "yzbqklnj"
input_str = "abcdef"
num = "609043"


def lowest_5_zero_num(input_str):
    num = -1
    flag = True
    while flag:
        num += 1
        num_string = str(num)

        test = hex(input_str, num_string)
        if test[:5] == "00000":
            flag = False
            return num


def lowest_6_zero_num(input_str):
    num = -1
    flag = True
    while flag:
        num += 1
        num_string = str(num)

        test = hex(input_str, num_string)
        if test[:6] == "000000":
            flag = False
            return num


def hex(input_str, num_string):
    combined_str = input_str + num_string
    return hashlib.md5(combined_str.encode("utf-8")).hexdigest()


# Test 1
assert lowest_5_zero_num("abcdef") == 609043

# Test 2
assert lowest_5_zero_num("pqrstuv") == 1048970

print("4.a", lowest_5_zero_num("yzbqklnj"))

print("4.b", lowest_6_zero_num("yzbqklnj"))
