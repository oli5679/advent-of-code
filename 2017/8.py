# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 11:27:28 2017

@author: oliver.cairns
"""
from utils import import_txt_file


def clean_data_fn(raw_data):
    instruction_list = [row.split(" ") for row in raw_data]
    letters = set(row[0] for row in instruction_list)
    letter_vals = {letter: 0 for letter in letters}
    return instruction_list, letter_vals


def assess_condition(instruction, values):
    if instruction[5] == "<":
        return values[instruction[4]] < int(instruction[6])

    if instruction[5] == "<=":
        return values[instruction[4]] <= int(instruction[6])

    if instruction[5] == ">":
        return values[instruction[4]] > int(instruction[6])

    if instruction[5] == ">=":
        return values[instruction[4]] >= int(instruction[6])

    if instruction[5] == "==":
        return values[instruction[4]] == int(instruction[6])

    if instruction[5] == "!=":
        return values[instruction[4]] != int(instruction[6])


def make_changes(instruction, values, assess_function):
    assessment = assess_function(instruction, values)
    if assessment:
        if instruction[1] == "inc":
            values[instruction[0]] += int(instruction[2])
        if instruction[1] == "dec":
            values[instruction[0]] -= int(instruction[2])
    return values


def make_all_changes(instructions, values, changes_function, assess_function):
    for instruction in instructions:
        values = changes_function(instruction, values, assess_function)
    return values


def find_max_following_all_changes(
    instructions, values, changes_function, assess_function
):
    highest = find_max_dict_value(values)
    for instruction in instructions:
        values = changes_function(instruction, values, assess_function)
        if find_max_dict_value(values) > highest:
            highest = find_max_dict_value(values)
    return highest


def find_max_dict_value(input_dict):
    return input_dict[max(input_dict, key=input_dict.get)]


problem_data_raw = import_txt_file("input_8.txt")

test_instructions_raw = [
    "b inc 5 if a > 1",
    "a inc 1 if b < 5",
    "c dec -10 if a >= 1",
    "c inc -20 if c == 10",
]

test_instructions, test_vals = clean_data_fn(test_instructions_raw)

assert not assess_condition(test_instructions[0], {"a": 0})
assert assess_condition(test_instructions[1], {"b": 0})
assert assess_condition(test_instructions[2], {"a": 1})
assert assess_condition(test_instructions[3], {"c": 10})


test_vals = make_changes(test_instructions[0], test_vals, assess_condition)
assert test_vals["a"] == 0

test_vals = make_changes(test_instructions[1], test_vals, assess_condition)
assert test_vals["a"] == 1

test_vals = make_changes(test_instructions[2], test_vals, assess_condition)
assert test_vals["c"] == 10

test_vals = make_changes(test_instructions[3], test_vals, assess_condition)
assert test_vals["c"] == -10

test_instructions, test_vals = clean_data_fn(test_instructions_raw)
final_vals = make_all_changes(
    test_instructions, test_vals, make_changes, assess_condition
)

assert final_vals["c"] == -10

problem_instructions, problem_vals = clean_data_fn(problem_data_raw)

final_vals = make_all_changes(
    problem_instructions, problem_vals, make_changes, assess_condition
)

print("8.a", find_max_dict_value(final_vals))

problem_instructions, problem_vals = clean_data_fn(problem_data_raw)

highest_ever = find_max_following_all_changes(
    problem_instructions, problem_vals, make_changes, assess_condition
)

print("8.b", highest_ever)
