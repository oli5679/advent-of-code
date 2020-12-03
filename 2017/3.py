# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 10:54:53 2017

@author: oliver.cairns
"""
import numpy as np


def make_spiral(n):
    latest = 5
    step = 3
    spiral = np.array([[4, 3], [1, 2]])
    while latest < n:
        first = np.array(np.arange(latest, latest + step - 1)[:, np.newaxis])

        latest = latest + step - 1
        spiral = np.concatenate((first, spiral), axis=1)
        second = np.array([np.arange(latest, latest + step)])

        spiral = np.concatenate((spiral, second), axis=0)

        latest = latest + step
        third = np.array(np.arange(latest + step - 1, latest - 1, -1)[:, np.newaxis])

        latest = latest + step
        spiral = np.concatenate((spiral, third), axis=1)

        fourth = np.array([np.arange(latest + step, latest - 1, -1)])

        spiral = np.concatenate((fourth, spiral), axis=0)
        latest = latest + step + 1

        step += 2

    return spiral


spiral = make_spiral(265149)

one_i_index = np.where(spiral == 1)[0][0]

one_j_index = np.where(spiral == 1)[1][0]

target_i_index = np.where(spiral == 265149)[0][0]

target_j_index = np.where(spiral == 265149)[1][0]

print("3.a", abs(one_i_index - target_i_index) + abs(one_j_index - target_j_index))
# 438

# part 2

spiral_2 = make_spiral(144)

empty_2 = np.zeros((12, 12))

empty_2_centre_x = np.where(spiral_2 == 1)[0][0]
empty_2_centre_y = np.where(spiral_2 == 1)[1][0]

empty_2[empty_2_centre_x][empty_2_centre_y] = 1


flag = True
num = 1

while flag:
    num += 1

    x_index = np.where(spiral_2 == num)[0][0]
    y_index = np.where(spiral_2 == num)[1][0]
    neighbour_total = empty_2[x_index][y_index + 1]
    neighbour_total += empty_2[x_index][y_index - 1]
    neighbour_total += empty_2[x_index + 1][y_index]
    neighbour_total += empty_2[x_index + 1][y_index + 1]
    neighbour_total += empty_2[x_index + 1][y_index - 1]
    neighbour_total += empty_2[x_index - 1][y_index]
    neighbour_total += empty_2[x_index - 1][y_index + 1]
    neighbour_total += empty_2[x_index - 1][y_index - 1]
    empty_2[x_index][y_index] = neighbour_total

    # print("num",num)
    if neighbour_total > 265149:
        print("3.b", int(neighbour_total))
        flag = False
