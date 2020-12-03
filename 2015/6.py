# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 10:52:44 2017

@author: oliver.cairns
"""
import numpy as np

lights_grid = np.zeros((1000, 1000))

text_file = open("input_6.txt", "r")
data = list(text_file.readlines())


def clean_data_and_count_lights(instructions, update_function):
    lights_grid = np.zeros((1000, 1000))

    # Cleaning, so can split on space
    clean_instructions = [r.replace("turn ", "turn").rstrip() for r in instructions]
    clean_instructions = [r.replace(" through ", " ") for r in clean_instructions]
    clean_instructions = [r.split(" ") for r in clean_instructions]

    for i in clean_instructions:
        lights_grid = update_function(lights_grid, i)

    return int(np.sum(lights_grid))


def update_lights(lights, instructions):
    action, start, end = instructions
    start_x, start_y = [int(num) for num in start.split(",")]
    end_x, end_y = [int(num) for num in end.split(",")]
    for x in range(start_x, end_x + 1):
        for y in range(start_y, end_y + 1):
            if action == "turnon":
                lights[x][y] = 1
            if action == "turnoff":
                lights[x][y] = 0
            if action == "toggle":
                lights[x][y] = 1 - lights[x][y]
    return lights


def update_lights_2(lights, instructions):
    action, start, end = instructions
    start_x, start_y = [int(num) for num in start.split(",")]
    end_x, end_y = [int(num) for num in end.split(",")]
    for x in range(start_x, end_x + 1):
        for y in range(start_y, end_y + 1):
            if action == "turnon":
                lights[x][y] += 1
            if action == "turnoff":
                lights[x][y] = max(lights[x][y] - 1, 0)
            if action == "toggle":
                lights[x][y] += 2
    return lights


assert (
    clean_data_and_count_lights(["turn on 0,0 through 999,999"], update_lights)
    == 1000000
)
assert clean_data_and_count_lights(["toggle 0,0 through 999,0"], update_lights) == 1000
assert (
    clean_data_and_count_lights(
        ["turn on 0,0 through 999,999", "turn off 499,499 through 500,500"],
        update_lights,
    )
    == 999996
)


print("6.a", clean_data_and_count_lights(data, update_lights))

assert clean_data_and_count_lights(["turn on 0,0 through 0,0"], update_lights_2) == 1
assert (
    clean_data_and_count_lights(
        ["turn on 0,0 through 0,0", "toggle 0,0 through 999,999"], update_lights_2
    )
    == 2000001
)

text_file = open("input_6.txt", "r")
data = list(text_file.readlines())


print("6.b", clean_data_and_count_lights(data, update_lights_2))
