#!/usr/bin/env python
"""24a-odds.py: Advent of Code Day 24: Never tell me the odds"""

__author__ = 'Mark Sun'

# Import utilities
from src import utilities as u


def process_stones(raw):
    stones = {}
    for i, s in enumerate(raw):
        [x, y, z] = [int(x) for x in s.strip().split('@')[0].split(',')]
        [vx, vy, _] = [int(x) for x in s.strip().split('@')[1].split(',')]
        m = vy/vx
        b = y-m*x
        dirx = vx//abs(vx)
        stones[i] = tuple([x, y, z, m, b, dirx])
    return stones


def is_xing(a, b):
    (xa, ya, za, ma, ba, dx) = a
    (xb, yb, zb, mb, bb, dx) = b
    if ma == mb:
        return None
    cross_x = (-bb+ba)/(-ma+mb)
    cross_y = (mb*ba-ma*bb)/(-ma+mb)
    return cross_x, cross_y


def count_xing(stones, area):
    ct = 0
    for a in list(stones.keys()):
        for b in list(stones.keys())[a:]:
            intersects = True
            xing = is_xing(stones[a], stones[b])
            if xing is None:
                continue
            if xing[0] > area[0][1] or xing[0] < area[0][0]:
                continue
            if xing[1] > area[1][1] or xing[1] < area[1][0]:
                continue
            for c in [a, b]:
                delta_x = int((xing[0]-stones[c][0])//abs(xing[0]-stones[c][0]))
                if delta_x != stones[c][-1]:
                    intersects = False
            if intersects:
                ct += 1
    print(ct)
    return ct


input_list = u.import_data('24')
input_stones = process_stones(input_list)
test_area = ((200000000000000, 400000000000000), (200000000000000, 400000000000000))
count_xing(input_stones, test_area)
