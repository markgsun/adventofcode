#!/usr/bin/env python
"""22b-slabs.py: Advent of Code Day 22: Sand Slabs"""

__author__ = 'Mark Sun'

# Import utilities
import utilities as u


def parse_bricks(bricks_raw):
    bricks_parsed = []
    for i, brick in enumerate(bricks_raw):
        bricks_parsed += [[[int(x) for x in brick.split('~')[0].split(',')],
                           [int(x) for x in brick.split('~')[1].split(',')]]]

    bricks_parsed = sorted(bricks_parsed, key=lambda x: x[0][2])

    bricks_dict = dict(zip(list(range(len(bricks_parsed))), bricks_parsed))
    return bricks_dict


def drop_bricks(bricks_in):
    x_max = max([x[0][0] for x in bricks_in.values()]+[x[1][0] for x in bricks_in.values()])
    y_max = max([x[0][1] for x in bricks_in.values()]+[x[1][1] for x in bricks_in.values()])

    # Stack: (coord x, coord y): [height, brick]
    stack = {}
    for x in range(x_max+1):
        for y in range(y_max+1):
            stack[(x, y)] = [0, -1]

    bricks_out = {}
    for k, brick in bricks_in.items():
        xrange = brick[1][0]-brick[0][0]
        yrange = brick[1][1]-brick[0][1]
        height = brick[1][2]-brick[0][2]+1

        below = []
        for x in range(xrange+1):
            for y in range(yrange+1):
                cube = [brick[0][0]+x, brick[0][1]+y]
                below += [stack[cube[0], cube[1]]]

        # Update brick position
        # Brick: [coord start, coord end, supports]
        y_end = max([x[0] for x in below])+1
        supports = set([x[1] for x in below if x[0] == y_end-1])
        brick_end = brick.copy()
        brick_end[0][2] = y_end
        brick_end[1][2] = brick_end[0][2]+brick[1][2]-brick[0][2]
        brick_end += [supports]
        bricks_out[k] = brick_end

        # Update stack heights
        for x in range(xrange+1):
            for y in range(yrange+1):
                stack_i = (brick[0][0]+x, brick[0][1]+y)
                stack[stack_i] = [y_end-1+height, k]

    return bricks_out


def count_bricks(bricks):
    safe = []
    supports = {}
    for k, brick in bricks.items():
        supporting = [i for i, x in bricks.items() if k in x[2]]
        supports[k] = supporting
        is_safe = True
        for x in supporting:
            if len(bricks[x][2]) == 1:
                is_safe = False
                break
        if is_safe:
            safe += [k]

    total = 0
    for k in bricks.keys()-safe:
        fall_bricks = []
        next_bricks = []
        for k2 in supports[k]:
            if len(bricks[k2][2]) == 1:
                next_bricks += [k2]
        while next_bricks:
            current = next_bricks.pop(0)
            if current not in fall_bricks:
                fall_bricks += [current]
                for k2 in supports[current]:
                    if all([x in fall_bricks for x in bricks[k2][2]]):
                        next_bricks += [k2]
        total += len(set(fall_bricks))
    print(total)
    return total


input_list = u.import_data('22')
input_bricks = parse_bricks(input_list)
dropped_bricks = drop_bricks(input_bricks)
count_bricks(dropped_bricks)
