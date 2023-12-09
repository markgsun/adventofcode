#!/usr/bin/env python
"""9a-mirage.py: Advent of Code Day 9: Mirage maintenance"""

__author__ = 'Mark Sun'

# Import utilities
import utilities as u

# Import input
input_list = u.import_data('9')


def get_deltas(history_in, deltas_in):
    deltas = []

    for i in range(len(history_in)-1):
        deltas += [history_in[i+1] - history_in[i]]

    deltas_out = deltas_in + [deltas]

    if not any(deltas):
        return deltas_out
    else:
        return get_deltas(deltas, deltas_out)


def extrapolate(deltas_in):
    deltas_rev = deltas_in[::-1]

    result = 0
    for row in deltas_rev:
        result += row[-1]
    return result


total = 0
for input_str in input_list:
    history_str = input_str.split()
    history = [int(x) for x in history_str]
    deltas_start = [history]
    total += extrapolate(get_deltas(history, deltas_start))

print(total)
