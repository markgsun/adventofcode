#!/usr/bin/env python
"""19a-aplenty.py: Advent of Code Day 19: Aplenty"""

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


def process_rules(part, workflow_id, workflows):
    workflow = workflows[workflow_id]
    next_id = None
    i = 0
    while next_id is None:
        rule = workflow[i]
        if len(rule) > 1:
            ops = {'<': lambda x: x < rule[2], '>': lambda x: x > rule[2]}
            rule_result = ops[rule[1]](part[rule[0]])
            if rule_result:
                next_id = rule[-1]
        else:
            next_id = rule[-1]
        i += 1

    if next_id in ['R', 'A']:
        return next_id

    return process_rules(part, next_id, workflows)


input_rules, input_parts = split_input(input_list)
total = 0
for input_part in input_parts:
    print(f'part: {input_part}')
    acceptance = process_rules(input_part, 'in', input_rules)
    print(f'final acceptance: {acceptance}')
    if acceptance == 'A':
        total += input_part['x'] + input_part['m'] + input_part['a'] + input_part['s']

print(total)
