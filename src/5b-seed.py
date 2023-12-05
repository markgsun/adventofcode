#!/usr/bin/env python
"""5a-seed.py: Advent of Code Day 5: If you give a seed a fertilizer"""

__author__ = 'Mark Sun'

# Import inputs
input_raw = open('../input/day5', 'r')
input_list = input_raw.read().split('\n')
unique_list = set(input_raw.read())
input_raw.close()

input_list = [x for x in input_list if x]
print(input_list)
seeds = [int(x) for x in input_list[0].split()[1:]]

# Initial seed bounds
seed_bnds = []
for j in range(len(seeds)):
    if j % 2 > 0:
        seed_bnds += [seeds[j - 1]]
        seed_bnds += [seeds[j - 1] + seeds[j] - 1]
print('seeds:{}'.format(seed_bnds))

temp_map = []
for i in input_list[2:]:
    i_split = i.split()

    if not i_split[0].isdigit():
        # Seed bounds
        for j in range(len(seed_bnds)):
            if j % 2 > 0:
                # Add extra seeds based on map boundaries:
                for map_item in temp_map:
                    if seed_bnds[j-1] < map_item[0] < seed_bnds[j]:
                        seed_bnds += [map_item[0], map_item[0] - 1]
                        print('+:{}'.format(map_item[0]))
                    if seed_bnds[j-1] < map_item[1] < seed_bnds[j]:
                        seed_bnds += [map_item[1], map_item[1] + 1]
                        print('+:{}'.format(map_item[1]))

        # Sort seeds and map
        seed_bnds.sort()
        temp_map.sort()
        print('origin seeds:{}'.format(seed_bnds))
        # Map seeds
        for j in range(len(seed_bnds)):
            for map_item in temp_map:
                if map_item[0] <= seed_bnds[j] <= map_item[1]:
                    seed_bnds[j] += map_item[2]
                    break
        print('map:{}'.format(temp_map))
        print('mapped seeds:{}\n\n'.format(seed_bnds))
        # Reset map
        temp_map = []
        continue
    else:
        orig_i = int(i_split[1])
        orig_f = orig_i + int(i_split[2]) - 1
        targ_i = int(i_split[0])
        temp_map += [[orig_i, orig_f, targ_i-orig_i]]

# Seed bounds
for j in range(len(seed_bnds)):
    if j % 2 > 0:
        # Add extra seeds and map boundaries:
        for map_item in temp_map:
            if seed_bnds[j - 1] < map_item[0] < seed_bnds[j]:
                seed_bnds += [map_item[0], map_item[0]]
                print('+:{}'.format(map_item[0]))
            if seed_bnds[j - 1] < map_item[1] < seed_bnds[j]:
                seed_bnds += [map_item[1], map_item[1]]
                print('+:{}'.format(map_item[1]))

# Dedupe and sort seeds and map
seed_bnds.sort()
temp_map.sort()
print('origin seeds:{}'.format(seed_bnds))
# Map seeds
for j in range(len(seed_bnds)):
    for map_item in temp_map:
        if map_item[0] <= seed_bnds[j] <= map_item[1]:
            seed_bnds[j] += map_item[2]
            break

print('map:{}'.format(temp_map))
print('final mapped seeds:{}'.format(seed_bnds))
seed_bnds.sort()
print('sorted mapped seeds:{}'.format(seed_bnds))
print(min(seed_bnds))

# Attempt: 34047950
# Attempt: 15880235
