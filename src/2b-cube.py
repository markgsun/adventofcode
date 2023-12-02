#!/usr/bin/env python
"""2a-trebuchet.py: Advent of Code Day 2: Cube Conundrum"""

__author__ = 'Mark Sun'


# Definitions
tot = {'red': 12, 'green': 13, 'blue': 14}

# Import inputs
inputRaw = open('../input/2a', 'r')
inputList = inputRaw.read().split('\n')
inputRaw.close()

total = 0
for itemStr in inputList:
    redList = itemStr.split(' red')
    redX = max([int(x[-2:]) for x in redList[:-1]])
    greenList = itemStr.split(' green')
    greenX = max([int(x[-2:]) for x in greenList[:-1]])
    blueList = itemStr.split(' blue')
    blueX = max([int(x[-2:]) for x in blueList[:-1]])

    total += redX*greenX*blueX

print(total)
