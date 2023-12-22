#!/usr/bin/env python
"""3a-gear.py: Advent of Code Day 3: Gear Ratios"""

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

for i in range(len(inputArr)):
    print(''.join(inputArr[i]))
    j = 0
    foundNum = '0'
    adj = []
    for j in range(len(inputArr[0])):
        testCd = inputArr[i][j]

        if testCd.isnumeric():
            adj += inputArr[max(i - 1, 0)][max(j - 1, 0):min(j + 1, jMax) + 1] +\
                   inputArr[i][max(j - 1, 0):min(j + 1, jMax) + 1] +\
                   inputArr[min(i + 1, iMax)][max(j - 1, 0):min(j + 1, jMax) + 1]

            foundNum += testCd

        else:
            if len([x for x in adj if not x.isnumeric() and x != '.']) > 0:
                total += int(foundNum)
                print('{},{}'.format(int(foundNum), total))

            foundNum = '0'
            adj = []

    if len([x for x in adj if not x.isnumeric() and x != '.']) > 0:
        total += int(foundNum)
        print('{},{}'.format(int(foundNum), total))


print('Total: {}'.format(total))
inputRaw = open('../input/3a', 'r')
uniqueList = list(set(inputRaw.read()))
uniqueList.sort()
inputRaw.close()
print(uniqueList)
