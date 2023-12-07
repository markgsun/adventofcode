#!/usr/bin/env python
"""7a-camel.py: Advent of Code Day 7: Camel cards"""

__author__ = 'Mark Sun'


def get_new_rank(hand_in):
    card_dict = {'A': 'Z', 'K': 'Y', 'Q': 'X', 'J': 'W', 'T': 'V'}

    cards = list(hand_in[0])
    card_ct = {}

    for card in cards:
        if card in card_ct.keys():
            card_ct[card] += 1
        else:
            card_ct[card] = 1

    if max(card_ct.values()) == 5:
        rank = 'Z'
    elif max(card_ct.values()) == 4:
        rank = 'Y'
    elif max(card_ct.values()) == 3:
        if min(card_ct.values()) == 2:
            rank = 'X'
        else:
            rank = 'W'
    elif max(card_ct.values()) == 2 and len(card_ct.keys()) == 3:
        rank = 'V'
    elif max(card_ct.values()) == 1:
        rank = 'T'
    else:
        rank = 'U'

    hand_des = hand_in[0]
    for src_card, des_card in card_dict.items():
        hand_des = hand_des.replace(src_card, des_card)

    return [rank+hand_des, hand_in[0], hand_in[1]]


# Import inputs
input_raw = open('../input/day7', 'r')
input_list = input_raw.read().split('\n')
unique_list = set(input_raw.read())
input_raw.close()

print(input_list)

hands = [[x.split()[0], int(x.split()[1])] for x in input_list]

print(hands)

new_hands = []
for hand in hands:
    new_hands += [get_new_rank(hand)]

total = 0
new_hands.sort(key=lambda x: x[0])
for i in range(len(new_hands)):
    total += (i+1) * new_hands[i][2]
    new_hands[i] = [(i+1) * new_hands[i][2]] + new_hands[i]

print(new_hands)
print(total)
