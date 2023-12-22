#!/usr/bin/env python
"""1a-trebuchet.py: Advent of Code Day 1: Trebuchet?!"""

__author__ = 'Mark Sun'


# Import input
inputRaw = open('../../input/day1', 'r')
inputList = inputRaw.read().split('\n')
inputRaw.close()

total = 0
for item in inputList:
    itemList: list[str] = list(item)
    numList: list[str] = [x for x in itemList if x.isnumeric()]
    numInt: int = int(numList[0] + numList[-1])
    total += numInt

print(total)
