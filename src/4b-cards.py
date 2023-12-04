#!/usr/bin/env python
"""4a-cards.py: Advent of Code Day 4: Scratchcards"""

__author__ = 'Mark Sun'

# Import inputs
input_raw = open('../input/4a', 'r')
input_list = input_raw.read().split('\n')
unique_list = set(input_raw.read())
input_raw.close()

total = 0
reps = [1]*len(input_list)

for card, input_str in enumerate(input_list):
    print(input_str)
    winning = [int(x) for x in input_str.split('|')[0].split(':')[1].split(' ') if x]
    win_dict = dict.fromkeys(winning, 0)
    number_list = [int(x) for x in input_str.split('|')[1].split(' ') if x]
    win_tot = 0
    for number in number_list:
        if number in win_dict:
            win_tot += 1
    if card < len(input_list)-1:
        reps[card+1:card+win_tot+1] = [x + reps[card] for x in reps[card+1:card+win_tot+1]]
    total += reps[card]

print(total)
