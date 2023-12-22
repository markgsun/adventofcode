#!/usr/bin/env python
"""7b-camel.py: Advent of Code Day 7: Camel cards"""

__author__ = 'Mark Sun'


def get_new_rank(hand_in):
    card_dict = {'A': 'Z', 'K': 'Y', 'Q': 'X', 'T': 'W', 'J': '0'}

    cards = list(hand_in[0])
    card_ct = {}

    for card in cards:
        if card in card_ct.keys():
            card_ct[card] += 1
        else:
            card_ct[card] = 1

    if max(card_ct.values()) == 5:                                  # Five of a kind    AAAAA
        rank = 'Z'
    elif max(card_ct.values()) == 4:                                # Four of a kind    AAAAB
        if 'J' in card_ct.keys() and card_ct['J'] == 4:             # Five of a kind    JJJJB
            rank = 'Z'
        elif 'J' in card_ct.keys() and card_ct['J'] == 1:           # Five of a kind    AAAAJ
            rank = 'Z'
        else:
            rank = 'Y'
    elif max(card_ct.values()) == 3:
        if min(card_ct.values()) == 2:                              # Full house        AAABB
            if 'J' in card_ct.keys() and card_ct['J'] == 3:         # Five of a kind    JJJBB
                rank = 'Z'
            elif 'J' in card_ct.keys() and card_ct['J'] == 2:       # Five of a kind    AAAJJ
                rank = 'Z'
            else:
                rank = 'X'
        else:                                                       # Three of a kind   AAABC
            if 'J' in card_ct.keys() and card_ct['J'] == 3:         # Four of a kind    JJJBC
                rank = 'Y'
            elif 'J' in card_ct.keys() and card_ct['J'] == 1:       # Four of a kind    AAAJC
                rank = 'Y'
            else:
                rank = 'W'
    elif (max(card_ct.values()) == 2 and
          len(card_ct.keys()) == 3):                                # Two Pair          AABBC
        if 'J' in card_ct.keys() and card_ct['J'] == 2:             # Four of a kind    JJBBC
            rank = 'Y'
        elif 'J' in card_ct.keys() and card_ct['J'] == 1:           # Full house        AABBJ
            rank = 'X'
        else:
            rank = 'V'
    elif max(card_ct.values()) == 1:                                # High Card         ABCDE
        if 'J' in card_ct.keys() and card_ct['J'] == 1:             # One Pair          JBCDE
            rank = 'U'
        else:
            rank = 'T'
    elif (max(card_ct.values()) == 2 and
          len(card_ct.keys()) == 4):                                # One Pair          AABCD
        if 'J' in card_ct.keys() and card_ct['J'] == 2:             # Three of a kind   JJBCD
            rank = 'W'
        elif 'J' in card_ct.keys() and card_ct['J'] == 1:           # Three of a kind   AAJCD
            rank = 'W'
        else:
            rank = 'U'
    else:
        rank = 'U'

    hand_des = hand_in[0]
    for src_card, des_card in card_dict.items():
        hand_des = hand_des.replace(src_card, des_card)

    return [rank+hand_des, hand_in[0], hand_in[1]]


# Import inputs
input_raw = open('../../input/day7', 'r')
input_list = input_raw.read().split('\n')
unique_list = set(input_raw.read())
input_raw.close()

hands = [[x.split()[0], int(x.split()[1])] for x in input_list]


new_hands = []
for hand in hands:
    new_hands += [get_new_rank(hand)]

total = 0
new_hands.sort(key=lambda x: x[0])
for i in range(len(new_hands)):
    total += (i+1) * new_hands[i][2]
    new_hands[i] = [(i+1) * new_hands[i][2]] + new_hands[i]

print(total)
