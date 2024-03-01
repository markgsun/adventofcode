#!/usr/bin/env python
"""10-cathode.py: Advent of Code Day 10: Cathode-Ray Tube"""

__author__ = 'Mark Sun'

# Import utilities
from src import utilities as u


class Solution:
    @staticmethod
    def signal_str(raw):
        ref = [20, 60, 100, 140, 180, 220]
        c = 0
        x = 1
        res = 0
        for instr in raw:
            if instr[:4] == 'addx':
                for _ in range(2):
                    c += 1
                    if c in ref:
                        res += c*x
                x += int(instr[5:])
            else:
                c += 1
                if c in ref:
                    res += c*x
        return res

    @staticmethod
    def crt(raw):
        c = 0
        x = 1
        scrn = ''
        for instr in raw:
            if instr[:4] == 'addx':
                for _ in range(2):
                    if len(scrn) == 40:
                        print(scrn)
                        scrn = ''
                        c = 0
                    if x in [c-1, c, c+1]:
                        scrn += '#'
                    else:
                        scrn += '.'
                    c += 1
                    # print(c, x, scrn[-1])
                x += int(instr[5:])
            else:
                if len(scrn) == 40:
                    print(scrn)
                    scrn = ''
                    c = 0
                if x in [c - 1, c, c + 1]:
                    scrn += '#'
                else:
                    scrn += '.'
                c += 1
        print(scrn)
        return None


input_list = u.import_data('2022', '10')
print(f'Part 1: {Solution.signal_str(input_list)}')
print(f'Part 2:')
Solution.crt(input_list)
