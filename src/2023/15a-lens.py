#!/usr/bin/env python
"""15a-lens.py: Advent of Code Day 15: Lens library"""

__author__ = 'Mark Sun'

# Import utilities
from src import utilities as u

# Import input
input_list = u.import_data('15')[0].split(',')

total = 0
for step in input_list:
    step_val = 0
    for c in step:
        val = ((step_val+ord(c))*17) % 256
        step_val = val
    total += step_val
print(total)
