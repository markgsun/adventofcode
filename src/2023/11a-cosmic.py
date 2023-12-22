#!/usr/bin/env python
"""11a-cosmic.py: Advent of Code Day 11: Cosmic expansion"""

__author__ = 'Mark Sun'

# Import utilities
from src import utilities as u

# Import input
input_list = u.import_data('11')

input_grid = []
for input_row in input_list:
    input_grid += [list(input_row)]

galaxies = []
for i, row in enumerate(input_grid):
    for j, cell in enumerate(row):
        if cell == '#':
            galaxies += [[i, j]]

empty_row = []
for i, _ in enumerate(input_grid):
    if not any([x[0] == i for x in galaxies]):
        empty_row += [i]

empty_col = []
for j, _ in enumerate(input_grid[0]):
    if not any([x[1] == j for x in galaxies]):
        empty_col += [j]

total = 0
for k1 in range(len(galaxies)):
    for k2 in range(k1+1, len(galaxies)):
        gal1 = galaxies[k1]
        gal2 = galaxies[k2]
        dist = abs(gal1[0]-gal2[0])+abs(gal1[1]-gal2[1])
        for r in empty_row:
            if min(gal1[0], gal2[0]) < r < max(gal1[0], gal2[0]):
                dist += 1
        for c in empty_col:
            if min(gal1[1], gal2[1]) < c < max(gal1[1], gal2[1]):
                dist += 1
        total += dist

print(total)
