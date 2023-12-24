#!/usr/bin/env python
"""2b-cube.py: Advent of Code Day 2: Cube Conundrum"""

__author__ = 'Mark Sun'


# Import inputs
inputRaw = open('../../input/day2', 'r')
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
