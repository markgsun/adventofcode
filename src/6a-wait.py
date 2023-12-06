#!/usr/bin/env python
"""6a-wait.py: Advent of Code Day 6: Wait for it"""

__author__ = 'Mark Sun'

# Import inputs
input_raw = open('../input/day6', 'r')
input_list = input_raw.read().split('\n')
unique_list = set(input_raw.read())
input_raw.close()

times = [int(x) for x in input_list[0].split()[1:]]
records = [int(x) for x in input_list[1].split()[1:]]
print('times:{}'.format(times))
print('distances:{}'.format(records))


def quad_solver(t, r):
    discr = (t ** 2 - 4 * r) ** 0.5
    return [(t - discr) / 2, (t + discr) / 2]


product = 1
for i in range(len(times)):
    win_range = quad_solver(times[i], records[i])
    win_int = [int(-(-win_range[0] // 1)), int(win_range[1] // 1)]
    if win_int[0] == win_range[0]:
        win_int[0] += 1
    if win_int[1] == win_range[1]:
        win_int[1] -= 1
    win_count = win_int[1] - win_int[0] + 1
    print(win_int)
    print(win_int[1] - win_int[0] + 1)
    product *= win_count

print(product)
