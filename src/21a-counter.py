#!/usr/bin/env python
"""21a-counter.py: Advent of Code Day 21: Step counter"""

__author__ = 'Mark Sun'

# Import utilities
import utilities as u


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
    while queue:
        current = queue.pop(0)
        if current[:-1] in visited:
            continue
        visited += [current[:-1]]
        if current[2] % 2 == 0:
            ct += 1
        if current[2] > 0:
            if current[0] > 0 and plot[current[0]-1][current[1]] != '#':
                queue += [(current[0]-1, current[1], current[2]-1)]
            if current[0] < len(plot)-1 and plot[current[0]+1][current[1]] != '#':
                queue += [(current[0]+1, current[1], current[2]-1)]
            if current[1] > 0 and plot[current[0]][current[1]-1] != '#':
                queue += [(current[0], current[1]-1, current[2]-1)]
            if current[1] < len(plot[0])-1 and plot[current[0]][current[1]+1] != '#':
                queue += [(current[0], current[1]+1, current[2]-1)]
    return ct


input_list = u.import_data('21')

steps_init = 64
start_pos = find_start(input_list)
final_ct = count_tiles(start_pos, input_list, steps_init)
print(final_ct)
