# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 17:18:14 2017

@author: oliver.cairns
"""

import csv

data = []
with open('input_2.txt', newline='') as inputfile:
    for row in csv.reader(inputfile):
        data.append(row)

#data = [["2x3x4"]]
#data = [["1x1x10"]]

clean_data = [[int(y) for y in x[0].split("x")] for x in data ]


def pres_vol(h,w,l):
    main = (2*l*w) + (2*w*h) + (2*h*l)
    slack = h*w*l/max([h,w,l])
    return int(main+slack)

def ribbon_len(h,w,l):
    main = 2*h + 2*w + 2*l - 2*max([h,w,l])
    bow = h*w*l
    return main + bow

area_total = 0
len_total = 0

for pres in clean_data:
    area_total += pres_vol(*pres)
    len_total += ribbon_len(*pres)
    
print("1.a",area_total)
print("1.b",len_total)