#!/usr/bin/env python
"""02-rock.py: Advent of Code Day 2: Rock Paper Scissors"""

__author__ = 'Mark Sun'

# Import utilities
from src import utilities as u


class Solution:
    @staticmethod
    def total_score1(raw):
        hier_dict = {'A': 'Y', 'B': 'Z', 'C': 'X'}
        eq_dict = {'A': 'X', 'B': 'Y', 'C': 'Z'}
        score_dict = {'X': 1, 'Y': 2, 'Z': 3}
        score = 0
        for rd in raw:
            [p1, p2] = rd.split(' ')
            score += score_dict[p2]
            if p2 == hier_dict[p1]:
                score += 6
            elif p2 == eq_dict[p1]:
                score += 3
        return score

    @staticmethod
    def total_score2(raw):
        hier_dict = {'A': 'B', 'B': 'C', 'C': 'A'}
        score_dict = {'X': 0, 'Y': 3, 'Z': 6, 'A': 1, 'B': 2, 'C': 3}
        score = 0
        for rd in raw:
            [p1, res] = rd.split(' ')
            score += score_dict[res]
            if res == 'X':
                p2 = list(hier_dict.keys())[list(hier_dict.values()).index(p1)]
            elif res == 'Y':
                p2 = p1
            else:
                p2 = hier_dict[p1]
            score += score_dict[p2]
        return score


input_list = u.import_data('2022', '2')
print(f'Part 1: {Solution.total_score1(input_list)}')
print(f'Part 2: {Solution.total_score2(input_list)}')
