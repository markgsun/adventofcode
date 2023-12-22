#!/usr/bin/env python
"""18a-lagoon.py: Advent of Code Day 18: Lavaduct lagoon"""

__author__ = 'Mark Sun'

# Import utilities
import utilities as u

# Import input
input_list = [x.split(' ') for x in u.import_data('18')]


def get_vertices(plan):
    vertices = [(0, 0)]

    bound = 0
    for row in plan:
        direction = row[0]
        units = int(row[1])
        bound += units
        if direction == 'R':
            vertices += [(vertices[-1][0], vertices[-1][1]+units)]
        if direction == 'L':
            vertices += [(vertices[-1][0], vertices[-1][1]-units)]
        if direction == 'D':
            vertices += [(vertices[-1][0]+units, vertices[-1][1])]
        if direction == 'U':
            vertices += [(vertices[-1][0]-units, vertices[-1][1])]
    return vertices, bound


def shoelace(vertices):
    total = 0
    for i in range(len(vertices)-1):
        if i < len(vertices)-1:
            total += vertices[i][0] * vertices[i+1][1]
            total -= vertices[i][1] * vertices[i+1][0]
    return abs(total//2)


def total_area(plan):
    all_vert, bound = get_vertices(plan)
    area = shoelace(all_vert)
    internal = area+1-bound/2
    print(internal+bound)


total_area(input_list)
