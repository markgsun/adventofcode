#!/usr/bin/env python
"""4a-cards.py: Advent of Code Day 4: Scratchcards"""

__author__ = 'Mark Sun'

# Import inputs
input_raw = open('../input/4ex', 'r')
input_list = input_raw.read().split('\n')
unique_list = set(input_raw.read())
input_raw.close()

total = 0
for input_str in input_list:
    print(input_str)
    winning = [int(x) for x in input_str.split('|')[0].split(':')[1].split(' ') if x]
    win_dict = dict.fromkeys(winning, 0)
    number_list = [int(x) for x in input_str.split('|')[1].split(' ') if x]
    win_tot = 0
    for number in number_list:
        if number in win_dict:
            win_tot += 1
    points = 0 if not win_tot else 2 ** (win_tot - 1)
    total += points
    print('winning:{}\nhave:{}\nwins:{}\npoints:{}\ntotal:{}'.format(win_dict, number_list, win_tot, points, total))
