#!/usr/bin/env python
"""19b-aplenty.py: Advent of Code Day 19: Aplenty"""

__author__ = 'Mark Sun'

# Import utilities
import utilities as u

# Import input
input_list = [x.split(' ') for x in u.import_data('19')]


def split_input(full_input):
    rules_raw = []
    parts_raw = []
    rulelist = True
    for row in full_input:
        if row == ['']:
            rulelist = False
            continue
        if rulelist:
            rules_raw += row
        else:
            parts_raw += row

    parts = []
    for part in parts_raw:
        part_dict = {}
        for attribute in part[1:-1].split(','):
            part_dict[attribute.split('=')[0]] = int(attribute.split('=')[1])
        parts += [part_dict]

    workflows = {}
    for rule in rules_raw:
        key = rule.split('{')[0]
        logic = rule.split('{')[1].split(',')
        rule_logics = []
        for lg in logic:
            if ':' in lg:
                category = lg[0]
                value = int(lg.split(':')[0][2:])
                comp = lg[1]
                dest = lg.split(':')[1]
                rule_logics += [[category, comp, value, dest]]
            else:
                rule_logics += [[lg[:-1]]]
        workflows[key] = rule_logics
    return workflows, parts


def copy_dict(ranges):
    output_ranges = {'x': [ranges['x'][0], ranges['x'][1]], 'm': [ranges['m'][0], ranges['m'][1]],
                     'a': [ranges['a'][0], ranges['a'][1]], 's': [ranges['s'][0], ranges['s'][1]]}
    return output_ranges


def process_rules(workflow_id, workflows, ranges):
    workflow = workflows[workflow_id]
    vol = 0

    for rule in workflow:
        next_id = rule[-1]
        next_ranges = copy_dict(ranges)
        if len(rule) > 1:
            if rule[1] == '>':
                next_ranges[rule[0]][0] = max(rule[2], ranges[rule[0]][0]) + 1
                ranges[rule[0]][1] = max(rule[2], ranges[rule[0]][0])
            if rule[1] == '<':
                next_ranges[rule[0]][1] = min(rule[2], ranges[rule[0]][1]) - 1
                ranges[rule[0]][0] = min(rule[2], ranges[rule[0]][1])

        if rule[-1] == 'A':
            vol += ((next_ranges['x'][1]-next_ranges['x'][0]+1) *
                    (next_ranges['m'][1]-next_ranges['m'][0]+1) *
                    (next_ranges['a'][1]-next_ranges['a'][0]+1) *
                    (next_ranges['s'][1]-next_ranges['s'][0]+1))
        elif rule[-1] != 'R':
            vol += process_rules(next_id, workflows, next_ranges)
    return vol


input_rules, _ = split_input(input_list)
ranges_start = {'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]}
total_vol = process_rules('in', input_rules, ranges_start)
print(total_vol)
