#!/usr/bin/env python
"""08-treetop.py: Advent of Code Day 8: Treetop Tree House"""

__author__ = 'Mark Sun'

# Import utilities
from src import utilities as u


class Solution:
    @staticmethod
    def viz_trees(raw, pt):
        n_col = len(raw[0])
        trees = (['-'*(n_col+2)] +
                 ['-'+x+'-' for x in raw] +
                 ['-'*(n_col+2)])

        n_row = len(raw)
        n_col = len(raw[0])
        ct = 0
        for i, line in enumerate(trees):
            if 0 < i <= n_row:
                for j, t in enumerate(line):
                    if 0 < j <= n_col:
                        if pt-1:
                            prod = 1
                            lists = [trees[i][1:j][::-1],
                                     [x[j] for x in trees[1:i]][::-1],
                                     trees[i][j+1:-1],
                                     [x[j] for x in trees[i+1:-1]]]
                            for list_l in lists:
                                bool_l = [x >= t for x in list_l]
                                n_l = bool_l.index(True)+1 if True in bool_l else len(bool_l)
                                prod *= n_l
                            ct = max(ct, prod)
                        else:
                            if (t > min(max(trees[i][:j]),
                                        max([x[j] for x in trees[:i]]),
                                        max(trees[i][j+1:]),
                                        max([x[j] for x in trees[i+1:]]))):
                                ct += 1
                                continue
        return ct


input_list = u.import_data('2022', '8')
print(f'Part 1: {Solution.viz_trees(input_list, 1)}')
print(f'Part 2: {Solution.viz_trees(input_list, 2)}')
