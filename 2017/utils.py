# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 13:40:03 2017

@author: oliver.cairns
"""


def import_txt_file(file_path):
    data = []
    with open(file_path, "r") as f:
        for line in f.readlines():
            data.append(line.strip())
    return data
