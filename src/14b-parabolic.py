#!/usr/bin/env python
"""14b-parabolic.py: Advent of Code Day 14: Parabolic reflector dish"""

__author__ = 'Mark Sun'

# Import utilities
import utilities as u

# Import input
input_list = u.import_data('14')


def print_platform(platform):
    for row in platform:
        print(row)
    print('\n\n')


def get_load(platform, direction):
    platform_out = None
    if direction == 'w':
        platform_out = get_load_west(platform)
    elif direction == 's':
        platform_out = get_load_west(rotate(platform, 1))
    elif direction == 'e':
        platform_out = get_load_west(rotate(platform, 2))
    elif direction == 'n':
        platform_out = get_load_west(rotate(platform, 3))
    return platform_out


def get_load_west(platform):
    max_load = len(platform[0])

    load_out = 0
    for row in platform:
        for i, rock in enumerate(row):
            if rock == 'O':
                load_out += max_load-i
    return load_out


def tilt(platform, direction):
    platform_out = None
    if direction == 'w':
        platform_out = tilt_west(platform)
    elif direction == 's':
        platform_out = rotate(tilt_west(rotate(platform, 1)), 3)
    elif direction == 'e':
        platform_out = rotate(tilt_west(rotate(platform, 2)), 2)
    elif direction == 'n':
        platform_out = rotate(tilt_west(rotate(platform, 3)), 1)
    return platform_out


def tilt_west(platform):
    platform_out = []
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
        row = row.replace('O', '.')
        for k in load.keys():
            row = row[:k + 1] + 'O' * load[k] + row[k + load[k] + 1:]
        platform_out += [row]
    return platform_out


def rotate(platform, n):
    platform_out = platform.copy()
    i = 0
    while i < n:
        platform_out = [''.join(x) for x in list(zip(*platform_out[::-1]))]
        i += 1
    return platform_out


def spin_cycle(platform):
    return tilt(tilt(tilt(tilt(platform, 'n'), 'w'), 's'), 'e')


def stress_test(platform, n):
    seen = []
    for i in range(n):
        platform = spin_cycle(platform)
        if platform in seen:
            cycle_start = seen.index(platform)
            cycle_len = i - cycle_start
            print('cycle detected: {} to {}'.format(cycle_start, i))
            cycles_remaining = (n-i) % cycle_len - 1
            for j in range(cycles_remaining):
                platform = spin_cycle(platform)
            load = get_load(platform, 'n')
            print(load)
            return load
        else:
            seen += [platform]


stress_test(input_list, 1000000000)

