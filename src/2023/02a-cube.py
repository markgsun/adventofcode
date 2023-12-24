#!/usr/bin/env python
"""2a-cube.py: Advent of Code Day 2: Cube Conundrum"""

__author__ = 'Mark Sun'


# Definitions
tot = {'red': 12, 'green': 13, 'blue': 14}

# Import inputs
inputRaw = open('../../input/day2', 'r')
inputList = inputRaw.read().split('\n')
inputRaw.close()

total = 0
for itemStr in inputList:
    gameCheck = True
    gameID = int(itemStr.split(':')[0].split(' ')[1])
    draws = itemStr.split(':')[1].split(';')
    for draw in draws:
        balls = draw.split(',')
        for ball in balls:
            numX = int(ball.split(' ')[1])
            color = ball.split(' ')[2]
            if numX > tot[color]:
                gameCheck = False
    if gameCheck:
        total += gameID

print(total)
