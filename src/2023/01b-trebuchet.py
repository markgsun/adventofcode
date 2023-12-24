#!/usr/bin/env python
"""1a-trebuchet.py: Advent of Code Day 1: Trebuchet?!"""

__author__ = 'Mark Sun'


# Definitions
findNums = ['0', 'zero', '1', 'one', '2', 'two',   '3', 'three', '4', 'four',
            '5', 'five', '6', 'six', '7', 'seven', '8', 'eight', '9', 'nine']
findNumsRev = [num[::-1] for num in findNums]

numDict = {'0': 0, 'zero': 0, '1': 1, 'one': 1, '2': 2, 'two': 2,   '3': 3, 'three': 3, '4': 4, 'four': 4,
           '5': 5, 'five': 5, '6': 6, 'six': 6, '7': 7, 'seven': 7, '8': 8, 'eight': 8, '9': 9, 'nine': 9}

# Import inputs
inputRaw = open('../../input/day1', 'r')
inputList = inputRaw.read().split('\n')
inputRaw.close()

total = 0
for itemStr in inputList:
    foundDict = {}
    for num in findNums:
        foundDict[num] = itemStr.find(num)

    foundDict = {key: value for key, value in foundDict.items() if value >= 0}
    firstNum = str(numDict[min(foundDict, key=foundDict.get)])

    itemStrRev = itemStr[::-1]
    foundDictRev = {}
    for num in findNumsRev:
        foundDictRev[num] = itemStrRev.find(num)

    foundDictRev = {key: value for key, value in foundDictRev.items() if value >= 0}
    lastNum = str(numDict[min(foundDictRev, key=foundDictRev.get)[::-1]])

    numResult = int(firstNum+lastNum)
    total += numResult

print(total)
