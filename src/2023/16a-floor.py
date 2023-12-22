#!/usr/bin/env python
"""16a-floor.py: Advent of Code Day 16: The floor will be lava"""

__author__ = 'Mark Sun'

# Import utilities
from src import utilities as u

# Import input
input_list = u.import_data('16')


def pad_input(grid_in):
    grid_out = (['o'*(len(grid_in[0])+2)] +
                ['o'+x+'o' for x in input_list] +
                ['o'*(len(grid_in[0])+2)])
    grid_out[1] = '-'+grid_out[1][1:]
    return grid_out


def count_tiles(grid, ct, loc, direction):
    i = loc[0]
    j = loc[1]
    mirror = grid[i][j]

    if mirror == 'o':
        return ct
    if mirror in ['|', '-'] and ct[i][j] == 1:
        return ct
    if ct[i][j] >= 4:
        return ct

    ct[i][j] += 1

    if mirror == '-':
        for j1 in range(j-1, 0, -1):
            if grid[i][j1] not in ['.', '-']:
                ct = count_tiles(grid, ct, [i, j1], 'w')
                break
            ct[i][j1] += 1
        for j1 in range(j+1, len(grid[0])):
            if grid[i][j1] not in ['.', '-']:
                ct = count_tiles(grid, ct, [i, j1], 'e')
                break
            ct[i][j1] += 1

    elif mirror == '|':
        for i1 in range(i-1, 0, -1):
            if grid[i1][j] not in ['.', '|']:
                ct = count_tiles(grid, ct, [i1, j], 'n')
                break
            ct[i1][j] += 1
        for i1 in range(i+1, len(grid)):
            if grid[i1][j] not in ['.', '|']:
                ct = count_tiles(grid, ct, [i1, j], 's')
                break
            ct[i1][j] += 1

    elif mirror == '/':
        if direction == 'e':
            for i1 in range(i-1, 0, -1):
                if grid[i1][j] not in ['.', '|']:
                    ct = count_tiles(grid, ct, [i1, j], 'n')
                    break
                ct[i1][j] += 1
        elif direction == 'w':
            for i1 in range(i+1, len(grid)):
                if grid[i1][j] not in ['.', '|']:
                    ct = count_tiles(grid, ct, [i1, j], 's')
                    break
                ct[i1][j] += 1
        elif direction == 's':
            for j1 in range(j-1, 0, -1):
                if grid[i][j1] not in ['.', '-']:
                    ct = count_tiles(grid, ct, [i, j1], 'w')
                    break
                ct[i][j1] += 1
        elif direction == 'n':
            for j1 in range(j+1, len(grid[0])):
                if grid[i][j1] not in ['.', '-']:
                    ct = count_tiles(grid, ct, [i, j1], 'e')
                    break
                ct[i][j1] += 1

    elif mirror == '\\':
        if direction == 'e':
            for i1 in range(i+1, len(grid)):
                if grid[i1][j] not in ['.', '|']:
                    ct = count_tiles(grid, ct, [i1, j], 's')
                    break
                ct[i1][j] += 1
        elif direction == 'n':
            for j1 in range(j-1, 0, -1):
                if grid[i][j1] not in ['.', '-']:
                    ct = count_tiles(grid, ct, [i, j1], 'w')
                    break
                ct[i][j1] += 1
        elif direction == 'w':
            for i1 in range(i-1, 0, -1):
                if grid[i1][j] not in ['.', '|']:
                    ct = count_tiles(grid, ct, [i1, j], 'n')
                    break
                ct[i1][j] += 1
        elif direction == 's':
            for j1 in range(j+1, len(grid[0])):
                if grid[i][j1] not in ['.', '-']:
                    ct = count_tiles(grid, ct, [i, j1], 'e')
                    break
                ct[i][j1] += 1

    return ct


grid_pad = pad_input(input_list)
grid_ct = [[0 for i in range(len(grid_pad[0]))] for j in range(len(grid_pad))]

final_ct = count_tiles(grid_pad, grid_ct, [1, 0], '')
total = -1
for row in final_ct:
    for tile in row:
        total += tile != 0

print(total)

