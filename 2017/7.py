# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 10:16:15 2017

@author: oliver.cairns
"""
from utils import import_txt_file
def clean_data_fn(data):
    all_vals= []
    clean_data = [row.split(" (") for row in data]
    clean_data = [[row[0]]+row[1].split(")") for row in clean_data]
    clean_data = {row[0]:[int(row[1]),row[2].replace(" -> ","").split(", ")] for row in clean_data}
    for key, value in clean_data.items():
        if value[1] == [""]:
            clean_data[key]=[value[0],[]]
        all_vals += clean_data[key][1]
    all_vals = set(all_vals)
    return clean_data, all_vals

def find_base(raw_data):
    clean_data,all_vals = clean_data_fn(raw_data)
    for key, value in clean_data.items():
            if value[1] != [""]:
                if key not in all_vals:
                    return key

def find_weight(node,clean_data):
    weight, above_nodes = clean_data[node]
    for node in above_nodes:
        weight += find_weight(node,clean_data)
    return weight

def find_imbalances(raw_data):
    clean_data, all_vals = clean_data_fn(raw_data)
    imbalances_details = []
    imbalances_list = []
    for key, value in clean_data.items():
        weights = []
        for above_node in value[1]:
            weights.append(find_weight(above_node,clean_data))
        if len(set(weights)) > 1:
            imbalances_details.append([key,weights,value[1]])
            imbalances_list.append(key)
    return imbalances_details,imbalances_list

def highest_imbalances(raw_data):
    all_imbalances_details, all_imbalances_list = find_imbalances(raw_data)
    highest_imbalances= []
    for imbalance in all_imbalances_details:
        flag = True
        for above_node in imbalance[2]:
            if above_node in all_imbalances_list:
                flag = False
        if flag:
            highest_imbalances.append(imbalance)
    return highest_imbalances

problem_data = import_txt_file('input_7.txt')


test_data = ["pbga (66)","xhth (57)","ebii (61)","havc (66)","ktlj (57)","fwft (72) -> ktlj, cntj, xhth", 
"qoyq (66)","padx (45) -> pbga, havc, qoyq","tknk (41) -> ugml, padx, fwft","jptl (61)",
"ugml (68) -> gyxo, ebii, jptl","gyxo (61)","cntj (57)"]


assert(find_base(test_data)) == "tknk"

print("7.a",find_base(problem_data))

clean_test_data, all_vals_test = clean_data_fn(test_data)

assert(find_weight("ebii",clean_test_data)) == 61
assert(find_weight("ugml",clean_test_data)) == 251
assert(find_weight("padx",clean_test_data)) == 243



assert highest_imbalances(test_data) == [['tknk', [251, 243, 243], ['ugml', 'padx', 'fwft']]]

print(highest_imbalances(problem_data))
print(clean_data_fn(problem_data)[0]['vrgxe'])
#From here it's simple maths. 1226 + 2159 - 2166 = 1219
