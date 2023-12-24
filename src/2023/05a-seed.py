#!/usr/bin/env python
"""5a-seed.py: Advent of Code Day 5: If you give a seed a fertilizer"""

__author__ = 'Mark Sun'

# Import inputs
input_raw = open('../../input/day5', 'r')
input_list = input_raw.read().split('\n')
unique_list = set(input_raw.read())
input_raw.close()

input_list = [x for x in input_list if x]
seeds = [int(x) for x in input_list[0].split()[1:]]

print(input_list)
temp_map = []
for i in input_list[2:]:
    i_split = i.split()
    if not i_split[0].isdigit():
        temp_map.sort()
        for j in range(len(seeds)):
            for map_item in temp_map:
                if map_item[0] <= seeds[j] <= map_item[1]:
                    seeds[j] += map_item[2]
                    break
        # Reset map
        temp_map = []
        continue
    else:
        orig_i = int(i_split[1])
        orig_f = orig_i + int(i_split[2]) - 1
        targ_i = int(i_split[0])
        temp_map += [[orig_i, orig_f, targ_i-orig_i]]

temp_map.sort()
for j in range(len(seeds)):
    for map_item in temp_map:
        if map_item[0] <= seeds[j] <= map_item[1]:
            seeds[j] += map_item[2]
            break

print(min(seeds))
