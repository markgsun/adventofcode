#!/usr/bin/env python
"""07-space.py: Advent of Code Day 7: No Space Left on Device"""

__author__ = 'Mark Sun'

# Import utilities
from src import utilities as u


class Solution:
    @staticmethod
    def count_size(raw, pt):
        # Path: {Type, Parent, Children, Size}
        dirs = {}
        curr_path = ''
        for line in raw:
            if '$ cd /' in line:
                curr_path = '~'
                dirs[curr_path] = 0
            elif '$ cd ..' in line:
                curr_path = '/'.join(curr_path.split('/')[:-1])
            elif '$ cd' in line:
                curr_path += '/'+line.split(' ')[-1]
                dirs[curr_path] = 0
            elif line[0].isnumeric():
                file_path = curr_path+'/'+line.split(' ')[-1]
                size = int(line.split(' ')[0])
                for k in dirs.keys():
                    if k in file_path:
                        dirs[k] += size
        if pt-1:
            res = min([x for x in list(dirs.values()) if x >= dirs['~']-40000000])
        else:
            res = sum([x for x in list(dirs.values()) if x <= 100000])
        return res


input_list = u.import_data('2022', '7')
print(f'Part 1: {Solution.count_size(input_list, 1)}')
print(f'Part 2: {Solution.count_size(input_list, 2)}')
