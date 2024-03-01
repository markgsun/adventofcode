#!/usr/bin/env python
"""11-monkey.py: Advent of Code Day 11: Monkey in the Middle"""

__author__ = 'Mark Sun'

# Import utilities
from src import utilities as u


class Solution:
    @staticmethod
    def monkey_biz(raw, pt):
        monkeys = {}
        dest = [0, 0]
        for line in raw:
            if 'Monkey' in line.split(' '):
                monkey = int(line.split(' ')[-1][:-1])
            elif 'Starting' in line.split(' '):
                items = [int(x) for x in line.split(': ')[-1].split(', ')]
            elif 'Operation:' in line.split(' '):
                op = line.split('= ')[-1].replace('old', 'x')
            elif 'Test:' in line.split(' '):
                test = int(line.split('by ')[-1])
            elif 'true:' in line.split(' '):
                dest[1] = int(line.split(' ')[-1])
            elif 'false:' in line.split(' '):
                dest[0] = int(line.split(' ')[-1])
            else:
                monkeys[monkey] = {'items': items, 'op': op, 'test': test, 'dest': dest.copy(), 'ct': 0}

        fct = 1
        for val in monkeys.values():
            fct *= val['test']
        ct = {key: 0 for key in monkeys.keys()}
        rd = 0
        max_rd = 10000 if pt-1 else 20
        while rd < max_rd:
            for m, val in monkeys.items():
                for i in val['items']:
                    i_new = (lambda x: eval(val['op']))(i) % fct if pt-1 else (lambda x: eval(val['op']))(i)//3
                    monkeys[val['dest'][i_new % val['test'] == 0]]['items'] += [i_new]
                    ct[m] += 1
                val['items'] = []
            rd += 1
        return sorted(ct.values())[-2]*sorted(ct.values())[-1]


input_list = u.import_data('2022', '11')
print(f'Part 1: {Solution.monkey_biz(input_list, 1)}')
print(f'Part 2: {Solution.monkey_biz(input_list, 2)}')
