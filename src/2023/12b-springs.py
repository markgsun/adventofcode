#!/usr/bin/env python
"""12b-springs.py: Advent of Code Day 12: Hot springs"""

__author__ = 'Mark Sun'

# Import utilities
from src import utilities as u

# Import input
input_list = u.import_data('12')

springs_raw = [list(x[0]) for x in [x.split() for x in input_list]]
groups_raw = [[int(y) for y in x[1].split(',')] for x in [x.split() for x in input_list]]

lines = [list(x) for x in zip(springs_raw, groups_raw)]


def get_permutations(springs, blocks, i, ib, ln):
    key = (i, ib, ln)
    if key in memo.keys():
        return memo[key]

    # End conditions
    if i == len(springs):
        if ib == len(blocks) and ln == 0:
            return 1
        elif ib == len(blocks)-1 and blocks[ib] == ln:
            return 1
        else:
            return 0
    # Recursion
    ct = 0
    a = 0
    b = 0
    if springs[i] == '.':
        if ln == 0:
            ct = get_permutations(springs, blocks, i+1, ib, ln)
        elif ln > 0 and ib < len(blocks) and ln == blocks[ib]:
            ct = get_permutations(springs, blocks, i+1, ib+1, 0)
    elif springs[i] == '#':
        ct = get_permutations(springs, blocks, i+1, ib, ln+1)
    elif springs[i] == '?':
        # Change to #
        a = get_permutations(springs, blocks, i+1, ib, ln+1)
        # Change to .
        if ln == 0:
            b = get_permutations(springs, blocks, i+1, ib, ln)
        elif ln > 0 and ib < len(blocks) and ln == blocks[ib]:
            b = get_permutations(springs, blocks, i+1, ib+1, 0)

        ct = a+b

    memo[key] = ct
    return ct


total = 0
for line in lines:
    memo = {}
    springs_in = ((line[0]+['?'])*5)[:-1]
    blocks_in = line[1]*5
    total += get_permutations(springs_in, blocks_in, 0, 0, 0)

print('total: {}'.format(total))
