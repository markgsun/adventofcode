#!/usr/bin/env python
"""flood_fill.py: test of dfs flood fill function"""

__author__ = 'Mark Sun'

# Import utilities
from src import utilities as u
import sys

# Import input
input_list = [x.split(' ') for x in u.import_data('18')]


def construct_grid(plan):
    max_ht = sum([int(x[1]) for x in plan if x[0] == 'R'])
    max_wt = sum([int(x[1]) for x in plan if x[0] == 'D'])
    grid = []
    for i in range(max_ht*2+3):
        grid += [['.']*(max_wt*2+3)]

    current = [max_ht+1, max_wt+1]
    grid[current[0]][current[1]] = '#'
    for step in plan:
        units = int(step[1])
        for i in range(units):
            if step[0] == 'R':
                current[1] = current[1]+1
            if step[0] == 'L':
                current[1] = current[1]-1
            if step[0] == 'D':
                current[0] = current[0]+1
            if step[0] == 'U':
                current[0] = current[0]-1

            grid[current[0]][current[1]] = '#'

    # truncate grid
    grid = [x for x in grid if '#' in x]
    left = min([x.index('#') for x in grid if '#' in x])
    right = min([x[::-1].index('#') for x in grid if '#' in x])
    grid = [x[left:-right] for x in grid]

    start = [0, 0]
    flag = False
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != '#' and grid[i][:j].count('#') == 1:
                start = [i, j]
                flag = True
                break
        if flag:
            break

    return grid, start


def dfs_fill(grid, point):
    if grid[point[0]][point[1]] == '#':
        return grid
    else:
        grid[point[0]][point[1]] = '#'
        grid = dfs_fill(grid, [point[0]+1, point[1]])
        grid = dfs_fill(grid, [point[0]-1, point[1]])
        grid = dfs_fill(grid, [point[0], point[1]+1])
        grid = dfs_fill(grid, [point[0], point[1]-1])

    return grid


grid_full, start_pt = construct_grid(input_list)
sys.setrecursionlimit(len(grid_full)*len(grid_full[0]))
grid_filled = dfs_fill(grid_full, start_pt)

for row_filled in grid_filled:
    print(row_filled)
