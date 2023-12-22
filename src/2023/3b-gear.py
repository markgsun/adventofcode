#!/usr/bin/env python
"""3b-gear.py: Advent of Code Day 3: Gear Ratios"""

__author__ = 'Mark Sun'

# Import inputs
inputRaw = open('../input/3a', 'r')
inputList = inputRaw.read().split('\n')
uniqueList = set(inputRaw.read())
inputRaw.close()
inputArr = [list(x) for x in inputList]

iMax = len(inputArr) - 1
jMax = len(inputArr[0]) - 1
total = 0
gearList = []
numberList = []
startInd = None

for i in range(len(inputArr)):
    print(inputArr[i])
    foundNum = '0'
    for j in range(len(inputArr[0])):
        testCd = inputArr[i][j]

        # Find gears
        if testCd == '*':
            gearList += [[i, j]]

        # Find numbers
        if testCd.isnumeric():
            if foundNum == '0':
                startInd = j
            foundNum += testCd
            if j == jMax:
                numberList += [[int(foundNum), i, startInd, j]]
                foundNum = '0'
        elif foundNum != '0':
            numberList += [[int(foundNum), i, startInd, j-1]]
            foundNum = '0'

for gear in gearList:
    adjNums = []
    for number in numberList:
        if min(gear[0] + 1, iMax) >= number[1] >= max(gear[0] - 1, 0):
            if min(gear[1] + 1, jMax) >= number[2] and number[3] >= max(gear[1] - 1, 0):
                adjNums += [number[0]]
    if len(adjNums) == 2:
        ratio = 1
        for num in adjNums:
            ratio *= num
        total += ratio


print('Gears: {}'.format(gearList))
print('Numbers: {}'.format(numberList))
print('Total: {}'.format(total))
