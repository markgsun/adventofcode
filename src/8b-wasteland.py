#!/usr/bin/env python
"""8b-wasteland.py: Advent of Code Day 8: Haunted wasteland"""

__author__ = 'Mark Sun'

# Import inputs
input_raw = open('../input/day8', 'r')
input_list = input_raw.read().split('\n')
unique_list = set(input_raw.read())
input_raw.close()

print(input_list)

instructions = input_list[0]
instr_len = len(instructions)
print(instructions)

nodes = {}
for input_str in input_list[2:]:
    node_key = input_str.split()[0]
    node_value = [input_str.split()[2].replace('(', '').replace(',', ''),
                  input_str.split()[3].replace(')', '')]
    nodes[node_key] = node_value

print(nodes)

# Determine starting keys
keys = []
for key in nodes.keys():
    if key[2] == 'A':
        keys += [key]
print(keys)

total = 0
i = 0
totals = [0 for x in keys]
while True:
    z_condition = [x[2] == 'Z' for x in keys]
    for j in range(len(z_condition)):
        if z_condition[j]:
            totals[j] = total

    if all([total != 0 for total in totals]):
        break
    if instructions[i] == 'R':
        keys = [nodes[key][1] for key in keys]
    else:
        keys = [nodes[key][0] for key in keys]

    total += 1
    if i == len(instructions)-1:
        i = 0
    else:
        i += 1

print(totals)

# TODO: Refactor LCM code
i = 1
while True:
    lcm = max(totals) * i
    if all([lcm % total == 0 for total in totals]):
        break
    i += 1
print(lcm)
