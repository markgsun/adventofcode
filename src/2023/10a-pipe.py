#!/usr/bin/env python
"""10a-pipe.py: Advent of Code Day 10: Pipe maze"""

__author__ = 'Mark Sun'

# Import utilities
from src import utilities as u

# Import input
input_list = u.import_data('10')

input_grid = []
for input_row in input_list:
    input_grid += [list(input_row)]

step_grid = [['.']*len(input_grid[0]) for _ in range(len(input_grid))]

# Find S in input:
s = [0, 0]
found = False
for i, row in enumerate(input_grid):
    for j, col in enumerate(row):
        if col == 'S':
            s = [i, j]
            step_grid[i][j] = 0
            found = True
            break
    if found:
        break

location = s
location_prev = s
step = 0
if not location[0] == 0 and input_grid[location[0]-1][location[1]] in ['7', 'F', '|']:
    location = [location[0]-1, location[1]]
elif not location[0] == len(input_grid)-1 and input_grid[location[0]+1][location[1]] in ['L', 'J', '|']:
    location = [location[0]+1, location[1]]
elif not location[1] == 0 and input_grid[location[0]][location[1]-1] in ['L', 'F', '-']:
    location = [location[0], location[1]-1]
elif not location[1] == len(input_grid[0])-1 and input_grid[location[0]][location[1]+1] in ['J', '7', '-']:
    location = [location[0], location[1]+1]

step += 1
step_grid[location[0]][location[1]] = step

while location != s:
    if location[0]-location_prev[0] == 1:       # Down
        if input_grid[location[0]][location[1]] == '|':
            location_prev = location.copy()
            location[0] += 1
        elif input_grid[location[0]][location[1]] == 'L':
            location_prev = location.copy()
            location[1] += 1
        elif input_grid[location[0]][location[1]] == 'J':
            location_prev = location.copy()
            location[1] -= 1
    elif location[0]-location_prev[0] == -1:    # Up
        if input_grid[location[0]][location[1]] == '|':
            location_prev = location.copy()
            location[0] -= 1
        elif input_grid[location[0]][location[1]] == 'F':
            location_prev = location.copy()
            location[1] += 1
        elif input_grid[location[0]][location[1]] == '7':
            location_prev = location.copy()
            location[1] -= 1
    elif location[1]-location_prev[1] == -1:    # Left
        if input_grid[location[0]][location[1]] == '-':
            location_prev = location.copy()
            location[1] -= 1
        elif input_grid[location[0]][location[1]] == 'F':
            location_prev = location.copy()
            location[0] += 1
        elif input_grid[location[0]][location[1]] == 'L':
            location_prev = location.copy()
            location[0] -= 1
    elif location[1]-location_prev[1] == 1:    # Right
        if input_grid[location[0]][location[1]] == '-':
            location_prev = location.copy()
            location[1] += 1
        elif input_grid[location[0]][location[1]] == 'J':
            location_prev = location.copy()
            location[0] -= 1
        elif input_grid[location[0]][location[1]] == '7':
            location_prev = location.copy()
            location[0] += 1
    step += 1
    step_grid[location[0]][location[1]] = step

print(step//2)