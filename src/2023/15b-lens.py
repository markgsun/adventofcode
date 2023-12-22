#!/usr/bin/env python
"""15a-lens.py: Advent of Code Day 15: Lens library"""

__author__ = 'Mark Sun'

# Import utilities
from src import utilities as u

# Import input
input_list = u.import_data('15')[0].split(',')


def hash_algo(step):
    step_val = 0
    for c in step:
        val = ((step_val+ord(c))*17) % 256
        step_val = val
    return step_val


boxes = {}
for i in range(256):
    boxes[i] = {}

for box_hash in input_list:
    box = hash_algo(box_hash.split('=')[0].split('-')[0])
    label = box_hash.split('=')[0].split('-')[0]
    if '=' in box_hash:
        lens = box_hash.split('=')[1]
        boxes[box][label] = lens
    else:
        lens = ''
        if label in boxes[box]:
            del boxes[box][label]

total = 0
for i in boxes:
    if boxes[i] != {}:
        power = 0
        for j, label in enumerate(boxes[i]):
            power += (i+1)*(j+1)*int(boxes[i][label])
        total += power
print(total)
