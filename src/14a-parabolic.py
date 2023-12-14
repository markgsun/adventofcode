#!/usr/bin/env python
"""14a-parabolic.py: Advent of Code Day 14: Parabolic reflector dish"""

__author__ = 'Mark Sun'

# Import utilities
import utilities as u

# Import input
input_list = u.import_data('14')


def tilt(platform_in, direction):
    if direction == 's':
        platform = rotate(platform_in, 1)
    elif direction == 'e':
        platform = rotate(platform_in, 2)
    elif direction == 'n':
        platform = rotate(platform_in, 3)
    else:
        platform = platform_in

    max_load = len(platform[0])

    total = 0
    for row in platform:
        curr_cube = -1
        load = {}
        for i, rock in enumerate(row):
            if rock == 'O':
                if curr_cube in load.keys():
                    load[curr_cube] += 1
                else:
                    load[curr_cube] = 1
            elif rock == '#':
                curr_cube = i
        for k in load.keys():
            load_i = sum([max_load-(k+x) for x in list(range(load[k]+1))][1:])
            total += load_i
    print(total)
    return None


def rotate(platform, n):
    i = 0
    while i < n:
        platform = [''.join(x) for x in list(zip(*platform[::-1]))]
        i += 1
    return platform


tilt(input_list, 'n')
