#!/usr/bin/env python
"""09-treetop.py: Advent of Code Day 9: Rope Bridge"""

__author__ = 'Mark Sun'

# Import utilities
from src import utilities as u


class Solution:
    @staticmethod
    def tail_pos(raw, rope_len):
        delts = {'R': [1,  0],
                 'L': [-1, 0],
                 'U': [0,  1],
                 'D': [0, -1]}
        rope = [[0, 0]]*rope_len
        visited = [rope[1]]
        for mv in raw:
            d = mv.split(' ')[0]
            for _ in range(int(mv.split(' ')[1])):
                rope[0] = [sum(x) for x in zip(rope[0], delts[d])]
                for node in range(rope_len-1):
                    dist = max(abs(rope[node][0]-rope[node+1][0]), abs(rope[node][1]-rope[node+1][1]))
                    if dist > 1:
                        dt = [int((rope[node][0]-rope[node+1][0])/max(1, abs(rope[node][0]-rope[node+1][0]))),
                              int((rope[node][1]-rope[node+1][1])/max(1, abs(rope[node][1]-rope[node+1][1])))]
                        rope[node+1] = [dt[0]+rope[node+1][0],
                                        dt[1]+rope[node+1][1]]
                if rope[-1] not in visited:
                    visited += [rope[-1]]
        return len(visited)


input_list = u.import_data('2022', '9')
print(f'Part 1: {Solution.tail_pos(input_list, 2)}')
print(f'Part 2: {Solution.tail_pos(input_list, 10)}')
