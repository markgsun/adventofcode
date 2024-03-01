#!/usr/bin/env python
"""06-tuning.py: Advent of Code Day 6: Tuning Trouble"""

__author__ = 'Mark Sun'

# Import utilities
from src import utilities as u


class Solution:
    @staticmethod
    def find_marker(raw, n):
        buffer = raw[0]
        loc = 0
        while loc+n-1 < len(buffer):
            if len(set(buffer[loc:loc+n])) == n:
                break
            loc += 1
        return loc + n


input_list = u.import_data('2022', '6')
print(f'Part 1: {Solution.find_marker(input_list, 4)}')
print(f'Part 2: {Solution.find_marker(input_list, 14)}')
