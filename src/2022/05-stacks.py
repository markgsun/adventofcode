#!/usr/bin/env python
"""05-stacks.py: Advent of Code Day 5: Supply Stacks"""

__author__ = 'Mark Sun'

# Import utilities
from src import utilities as u


class Solution:
    def __init__(self, raw):
        split_ind = raw.index('')
        stacks_raw = raw[:split_ind]
        moves_raw = raw[split_ind+1:]
        key_list = [int(x) for x in stacks_raw[-1].split('  ')]
        stacks = {key: [] for key in key_list}
        for s in stacks_raw[:-1]:
            for k in key_list:
                i = 1+4*(k-1)
                if i >= len(s)-1:
                    continue
                if s[i] != ' ':
                    stacks[k] += [s[i]]
        self.stacks = stacks

        moves = []
        for move in moves_raw:
            num = int(move.split(' from ')[0][-2:])
            src = int(move.split(' from ')[1][0])
            des = int(move.split(' from ')[1][-1])
            moves += [[num, src, des]]
        self.moves = moves

    def move_blocks(self, move_i, pt):
        [num, src, des] = self.moves[move_i]
        for i in range(num):
            tmp = self.stacks[src].pop(0)
            if pt-1:
                self.stacks[des].insert(i, tmp)
            else:
                self.stacks[des].insert(0, tmp)

    def find_tops(self, pt):
        for i, move in enumerate(self.moves):
            self.move_blocks(i, pt)
        return ''.join([self.stacks[k][0] for k in self.stacks.keys()])


input_list = u.import_data('2022', '5')
sol = Solution(input_list)
print(f'Part 1: {sol.find_tops(1)}')
sol = Solution(input_list)
print(f'Part 2: {sol.find_tops(2)}')
