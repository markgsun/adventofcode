#!/usr/bin/env python
"""8a-wasteland.py: Advent of Code Day 8: Haunted wasteland"""

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

total = 0
i = 0
key = 'AAA'
while True:
    print(key)
    if key == 'ZZZ':
        break
    if instructions[i] == 'R':
        key = nodes[key][1]
    else:
        key = nodes[key][0]

    total += 1
    if i == len(instructions)-1:
        i = 0
    else:
        i += 1

print(total)
