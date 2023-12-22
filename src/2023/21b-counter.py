#!/usr/bin/env python
"""21b-counter.py: Advent of Code Day 21: Step counter"""

__author__ = 'Mark Sun'

# Import utilities
from src import utilities as u


def find_start(plots):
    for i, row in enumerate(plots):
        if 'S' in row:
            j = row.index('S')
            result = (i, j)
            return result
    raise Exception('No start position detected')


def count_tiles(pos, plot, steps):
    queue = [pos+tuple([steps])]
    visited = []
    ct = 0
    deltas = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    while queue:
        current = queue.pop(0)
        if current[:-1] in visited:
            continue
        visited += [current[:-1]]
        if current[2] % 2 == 0:
            ct += 1
        if current[2] > 0:
            for delta in deltas:
                next_pos = (current[0]+delta[0], current[1]+delta[1], current[2]-1)
                tile = plot[next_pos[0] % len(plot)-len(plot)][next_pos[1] % len(plot[0])-len(plot[0])]
                if tile != '#':
                    queue += [next_pos]

    return ct


def count_tiles_full(pos, plot):
    queue = [pos+tuple([0])]
    visited = {}
    deltas = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    while queue:
        current = queue.pop(0)
        if current[:-1] in visited.keys():
            continue
        visited[current[:-1]] = current[2]
        for delta in deltas:
            next_pos = (current[0] + delta[0], current[1] + delta[1], current[2]+1)
            if next_pos[0] < 0 or next_pos[0] >= len(plot) or next_pos[1] < 0 or next_pos[1] >= len(plot[0]):
                continue
            else:
                tile = plot[next_pos[0]][next_pos[1]]
                if tile != '#':
                    queue += [next_pos]

    return visited


input_list = u.import_data('21')

steps_init = 65
start_pos = find_start(input_list)
final_ct = count_tiles(start_pos, input_list, steps_init)

# 3759,33496,92857
# 14812x^2+14925x+3759
print(14812*202300**2+14925*202300+3759)
