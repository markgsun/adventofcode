#!/usr/bin/env python
"""12a-springs.py: Advent of Code Day 12: Hot springs"""

__author__ = 'Mark Sun'

# Import utilities
from src import utilities as u

# Import input
input_list = u.import_data('12')

records = [list(x[0]) for x in [x.split() for x in input_list]]
groups = [[int(y) for y in x[1].split(',')] for x in [x.split() for x in input_list]]
lines = [list(x) for x in zip(records, groups)]


def get_groups(springs_in):
    blocks_out = []
    pos = 0
    while pos < len(springs_in):
        block_len = 1
        if springs_in[pos] in ['#']:
            pos2 = pos + 1
            while pos2 < len(springs_in):
                if springs_in[pos2] == springs_in[pos]:
                    block_len += 1
                    pos2 += 1
                else:
                    break
            blocks_out += [block_len]
        pos += block_len
    return blocks_out


def get_permutations(index_in, line_in):
    springs_in = line_in[0]
    groups_in = line_in[1]
    ct = 0
    springs_a = springs_in.copy()
    springs_b = springs_in.copy()

    springs_a[index_in] = '#'
    springs_b[index_in] = '.'

    if '?' not in springs_a:
        ct += int(get_groups(springs_a) == groups_in)
        ct += int(get_groups(springs_b) == groups_in)
        # print('ct: {}, a: {}, b: {}'.format(ct, springs_a, springs_b))
    else:
        index_new = springs_a.index('?')
        ct += get_permutations(index_new, [springs_a, groups_in])
        ct += get_permutations(index_new, [springs_b, groups_in])
    return ct


total = 0
for line in lines:
    total += get_permutations(line[0].index('?'), line)

print('total: {}'.format(total))
