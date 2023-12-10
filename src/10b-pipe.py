#!/usr/bin/env python
"""10b-pipe.py: Advent of Code Day 10: Pipe maze"""

__author__ = 'Mark Sun'

# Import utilities
import utilities as u

# Import input
input_list = u.import_data('10')

input_grid = []
for input_row in input_list:
    input_grid += [list(input_row)]

clean_grid = [['.']*len(input_grid[0]) for _ in range(len(input_grid))]

# Find S in input:
# vertices = []
s = [0, 0]
found = False
for i, row in enumerate(input_grid):
    for j, col in enumerate(row):
        if col == 'S':
            s = [i, j]
            found = True
            break
    if found:
        break

location = s
# vertices += [location]
location_prev = s
step = 0
clean_grid[location[0]][location[1]] = input_grid[location[0]][location[1]]
if not location[0] == 0 and input_grid[location[0]-1][location[1]] in ['7', 'F', '|']:
    location = [location[0]-1, location[1]]
elif not location[0] == len(input_grid)-1 and input_grid[location[0]+1][location[1]] in ['L', 'J', '|']:
    location = [location[0]+1, location[1]]
elif not location[1] == 0 and input_grid[location[0]][location[1]-1] in ['L', 'F', '-']:
    location = [location[0], location[1]-1]
elif not location[1] == len(input_grid[0])-1 and input_grid[location[0]][location[1]+1] in ['J', '7', '-']:
    location = [location[0], location[1]+1]
step += 1

while location != s:
    clean_grid[location[0]][location[1]] = input_grid[location[0]][location[1]]

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

# Expand grid
exp_grid = []
for row in clean_grid:
    exp_row = []
    for cell in row:
        exp_row += (cell + ',')
    exp_grid += [exp_row] + [[',']*len(exp_row)]

# Fill expanded grid
for i in range(len(exp_grid)):
    for j in range(len(exp_grid[0])):
        if exp_grid[i][j] == ',':
            if i < len(exp_grid) - 1 and exp_grid[i+1][j] in ['|', 'L', 'J']:
                exp_grid[i][j] = '|'
            elif j < len(exp_grid[0]) - 1 and exp_grid[i][j+1] in ['-', 'J', '7']:
                exp_grid[i][j] = '-'
            elif i > 0 and exp_grid[i-1][j] in ['|', '7', 'F']:
                exp_grid[i][j] = '|'
            elif j > 0 and exp_grid[i][j-1] in ['-', 'L', 'F']:
                exp_grid[i][j] = '-'
            else:
                exp_grid[i][j] = '.'

clean_grid = exp_grid.copy()
ct = 0
while ct < 1000:
    # Down sweep
    for i in range(len(clean_grid)):
        for j in range(len(clean_grid[0])):
            if clean_grid[i][j] == '.':
                if i == 0 or clean_grid[i-1][j] == 'O':
                    clean_grid[i][j] = 'O'

    # Up sweep
    for i in reversed(range(len(clean_grid))):
        for j in range(len(clean_grid[0])):
            if clean_grid[i][j] == '.':
                if i == len(clean_grid)-1 or clean_grid[i+1][j] == 'O':
                    clean_grid[i][j] = 'O'

    # Right sweep
    for j in range(len(clean_grid[0])):
        for i in range(len(clean_grid)):
            if clean_grid[i][j] == '.':
                if j == 0 or clean_grid[i][j-1] == 'O':
                    clean_grid[i][j] = 'O'

    # Left sweep
    for j in reversed(range(len(clean_grid[0]))):
        for i in range(len(clean_grid)):
            if clean_grid[i][j] == '.':
                if j == len(clean_grid[0])-1 or clean_grid[i][j+1] == 'O':
                    clean_grid[i][j] = 'O'

    ct += 1

    # if clean_grid == clean_grid_temp:
    #     break

# Shrink grid
final_grid = []
for row in clean_grid[::2]:
    final_row = row[::2]
    final_grid += [final_row]

total = 0
for row in final_grid:
    # print(row)
    total += sum(x == '.' for x in row)

print(total)

# Attempt: 863 too high
# Attempt: 773 too high
