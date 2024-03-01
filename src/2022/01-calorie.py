#!/usr/bin/env python
"""01-calorie.py: Advent of Code Day 1: Calorie Counting"""

__author__ = 'Mark Sun'

# Import utilities
from src import utilities as u


class Solution:
    @staticmethod
    def most_calories(raw):
        cals, cals_max = 0, 0
        for item in raw:
            if item == '':
                cals_max = max(cals, cals_max)
                cals = 0
                continue
            cals += int(item)
        return cals_max

    @staticmethod
    def top3_calories(raw):
        cals, cals_top3 = 0, []
        for item in raw:
            if item == '':
                if len(cals_top3) < 3:
                    cals_top3 += [cals]
                elif int(cals) > min(cals_top3):
                    cals_top3.remove(min(cals_top3))
                    cals_top3 += [cals]
                cals = 0
                continue
            cals += int(item)

        return sum([int(x) for x in cals_top3])


input_list = u.import_data('2022', '1')
print(f'Part 1: {Solution.most_calories(input_list)}')
print(f'Part 2: {Solution.top3_calories(input_list)}')
