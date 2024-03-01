#!/usr/bin/env python
"""04-camp.py: Advent of Code Day 4: Camp Cleanup"""

__author__ = 'Mark Sun'

# Import utilities
from src import utilities as u


class Solution:
    @staticmethod
    def countpairs(raw, pt):
        ct = 0
        for pair in raw:
            r1 = [int(x) for x in pair.split(',')[0].split('-')]
            r2 = [int(x) for x in pair.split(',')[1].split('-')]
            if pt-1:
                if (((r1[0] <= r2[0]) & (r1[1] >= r2[0])) |
                    ((r2[0] <= r1[0]) & (r2[1] >= r1[0])) |
                    ((r1[1] >= r2[1]) & (r1[0] <= r2[1])) |
                    ((r2[1] >= r1[1]) & (r2[0] <= r1[1]))):
                    ct += 1
            else:
                if ((r1[0] <= r2[0]) & (r1[1] >= r2[1])) | ((r2[0] <= r1[0]) & (r2[1] >= r1[1])):
                    ct += 1
        return ct


input_list = u.import_data('2022', '4')
print(f'Part 1: {Solution.countpairs(input_list, 1)}')
print(f'Part 2: {Solution.countpairs(input_list, 2)}')
