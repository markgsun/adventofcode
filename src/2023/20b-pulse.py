#!/usr/bin/env python
"""20b-pulse.py: Advent of Code Day 20: Pulse propagation"""

__author__ = 'Mark Sun'

# Import utilities
from src import utilities as u

# Import input
input_list = u.import_data('20')


def create_modules(sequence_in):
    modules = {}
    for sequence_row in sequence_in:
        mod_type = sequence_row.split(' -> ')[0][0]
        mod = sequence_row.split(' -> ')[0][1:]
        dest = sequence_row.split(' -> ')[1].split(', ')
        if mod_type+mod == 'broadcaster':
            modules[mod_type + mod] = [mod_type+mod, 'low', dest]
        if mod_type == '%':
            modules[mod] = [mod_type, 'off', dest]
        if mod_type == '&':
            memory = {}
            for row2 in sequence_in:
                if mod in row2.split(' -> ')[1].split(', '):
                    memory[row2.split(' -> ')[0][1:]] = 'low'
            modules[mod] = [mod_type, memory, dest]

    return modules


def process_signal(signal_in, mod_in, mod, tgt, queue):
    if mod == tgt and signal_in == 'low':
        return True
    if mod in sequence:
        add_queue = True
        dests = sequence[mod][-1]
        signal_out = ''
        if mod == 'output':
            add_queue = False
        if sequence[mod][0] == 'broadcaster':
            signal_out = 'low'
        if sequence[mod][0] == '%':
            if signal_in == 'low':
                if sequence[mod][1] == 'off':
                    sequence[mod][1] = 'on'
                    signal_out = 'high'
                elif sequence[mod][1] == 'on':
                    sequence[mod][1] = 'off'
                    signal_out = 'low'
            else:
                add_queue = False
        if sequence[mod][0] == '&':
            sequence[mod][1][mod_in] = signal_in
            memory = sequence[mod][1]
            if all([memory[x] == 'high' for x in memory.keys()]):
                signal_out = 'low'
            else:
                signal_out = 'high'

        if add_queue:
            queue += [mod+' > '+signal_out+' > '+x for x in dests]

    if mod != 'broadcaster' and len(queue) == 0:
        return False

    next_signal = queue.pop(0)

    return process_signal(next_signal.split(' > ')[1], next_signal.split(' > ')[0],
                          next_signal.split(' > ')[2], tgt, queue)


def find_target(tgt):
    ct = 0
    found = False
    while not found:
        ct += 1
        found = process_signal('low', '', 'broadcaster', tgt, [])
    return ct


def prime_factors(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1

    return factors


def lcm(nums):
    prime_dict = {}
    for num in nums:
        factor_dict = {}
        for factor in prime_factors(num):
            if factor in factor_dict.keys():
                factor_dict[factor] += 1
            else:
                factor_dict[factor] = 1

        for factor in factor_dict.keys():
            if factor in prime_dict.keys():
                prime_dict[factor] = max(prime_dict.get(factor), factor_dict.get(factor))
            else:
                prime_dict[factor] = factor_dict.get(factor)

    res = 1
    for factor in prime_dict.keys():
        res *= factor ** prime_dict[factor]

    return res


cts = []
for target in ['nd', 'pc', 'vd', 'tx']:
    sequence = create_modules(input_list)
    cts += [find_target(target)]

print(lcm(cts))


