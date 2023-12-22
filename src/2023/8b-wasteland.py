#!/usr/bin/env python
"""8b-wasteland.py: Advent of Code Day 8: Haunted wasteland"""

__author__ = 'Mark Sun'

# Import inputs
input_raw = open('../../input/day8', 'r')
input_list = input_raw.read().split('\n')
unique_list = set(input_raw.read())
input_raw.close()

instructions = input_list[0]
instr_len = len(instructions)

nodes = {}
for input_str in input_list[2:]:
    node_key = input_str.split()[0]
    node_value = [input_str.split()[2].replace('(', '').replace(',', ''),
                  input_str.split()[3].replace(')', '')]
    nodes[node_key] = node_value

# Determine starting keys
keys = []
for key in nodes.keys():
    if key[2] == 'A':
        keys += [key]

total = 0
i = 0
totals = [0 for x in keys]
while True:
    z_condition = [x[2] == 'Z' for x in keys]
    for j in range(len(z_condition)):
        if z_condition[j]:
            totals[j] = total

    if all([total != 0 for total in totals]):
        break
    if instructions[i] == 'R':
        keys = [nodes[key][1] for key in keys]
    else:
        keys = [nodes[key][0] for key in keys]

    total += 1
    if i == len(instructions)-1:
        i = 0
    else:
        i += 1


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


print(lcm(totals))
