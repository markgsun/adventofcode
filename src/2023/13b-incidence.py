#!/usr/bin/env python
"""13b-incidence.py: Advent of Code Day 13: Point of incidence"""

__author__ = 'Mark Sun'

# Import utilities
from src import utilities as u

# Import input
input_list = u.import_data('13')

maps = []
map_temp = []
for input_row in input_list:
    if input_row == '':
        maps += [map_temp]
        map_temp = []
    else:
        map_temp += [input_row]
maps += [map_temp]


def find_vert(map_in):
    for p1 in range(1, len(map_in[0])):
        if p1 < len(map_in[0])/2:
            bef = [x[:p1] for x in map_in]
            aft = [x[p1:2*p1][::-1] for x in map_in]
        else:
            bef = [x[p1-(len(map_in[0])-p1):p1] for x in map_in]
            aft = [x[p1:][::-1] for x in map_in]
        if map_delta(bef, aft) == 1:
            return p1
    return 0


def find_horz(map_in):
    for p1 in range(1, len(map_in)):
        if p1 < len(map_in)/2:
            bef = map_in[:p1]
            aft = map_in[p1:2*p1][::-1]
        else:
            bef = map_in[p1-(len(map_in)-p1):p1]
            aft = map_in[p1:][::-1]
        if map_delta(bef, aft) == 1:
            return p1
    return 0


def map_delta(a, b):
    delta = 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] != b[i][j]:
                delta += 1
    return delta


total = 0
for curr_map in maps:
    total += find_vert(curr_map)+find_horz(curr_map)*100
print(total)
