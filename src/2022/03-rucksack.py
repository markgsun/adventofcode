#!/usr/bin/env python
"""03-rucksack.py: Advent of Code Day 3: Rucksack Reorganization"""

__author__ = 'Mark Sun'

# Import utilities
from src import utilities as u


class Solution:
    @staticmethod
    def priorities1(raw):
        score = 0
        for sack in raw:
            interx = list(set(sack[:int(len(sack)/2)]) & set(sack[int(len(sack)/2):]))[0]
            if interx.isupper():
                score += ord(interx)-(65-27)
            else:
                score += ord(interx)-(112-16)
        return score

    @staticmethod
    def priorities2(raw):
        score = 0
        group = []
        for n, sack in enumerate(raw):
            group += [sack]
            if n % 3 != 2:
                continue
            interx = list(set(group[0]) & set(group[1]) & set(group[2]))[0]
            if interx.isupper():
                score += ord(interx)-(65-27)
            else:
                score += ord(interx)-(112-16)
            group = []
        return score


input_list = u.import_data('2022', '3')
print(f'Part 1: {Solution.priorities1(input_list)}')
print(f'Part 2: {Solution.priorities2(input_list)}')
