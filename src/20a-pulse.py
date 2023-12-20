#!/usr/bin/env python
"""20a-pulse.py: Advent of Code Day 20: Pulse propagation"""

__author__ = 'Mark Sun'

# Import utilities
import utilities as u

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


def process_signal(signal_in, mod_in, mod, queue, ct):
    ct[signal_in] += 1

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
        return ct

    next_signal = queue.pop(0)

    return process_signal(next_signal.split(' > ')[1], next_signal.split(' > ')[0],
                          next_signal.split(' > ')[2], queue, ct)


sequence = create_modules(input_list)

ct_total = {'low': 0, 'high': 0}
for _ in range(1000):
    ct_push = process_signal('low', '', 'broadcaster', [], {'low': 0, 'high': 0})
    ct_total['low'] += ct_push['low']
    ct_total['high'] += ct_push['high']
print(ct_total['low']*ct_total['high'])
