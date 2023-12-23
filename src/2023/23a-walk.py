#!/usr/bin/env python
"""23a-walk.py: Advent of Code Day 23: A long walk"""

__author__ = 'Mark Sun'

# Import utilities
from src import utilities as u
import sys
sys.setrecursionlimit(1000000)


def walk_dfs(pos, grid, dist, visited):
    if pos == end_pos:
        return dist

    neighbors = []
    if grid[pos[0]][pos[1]] == '.':
        neighbors += [(pos[0]-1, pos[1]), (pos[0]+1, pos[1]), (pos[0], pos[1]-1), (pos[0], pos[1]+1)]
    if grid[pos[0]][pos[1]] == '^':
        neighbors += [(pos[0]-1, pos[1])]
    if grid[pos[0]][pos[1]] == 'v':
        neighbors += [(pos[0]+1, pos[1])]
    if grid[pos[0]][pos[1]] == '<':
        neighbors += [(pos[0], pos[1]-1)]
    if grid[pos[0]][pos[1]] == '>':
        neighbors += [(pos[0], pos[1]+1)]
    res_best = None
    for neighbor in neighbors:
        if neighbor in visited or grid[neighbor[0]][neighbor[1]] == '#':
            continue
        visited += [neighbor]
        res_temp = walk_dfs(neighbor, grid, dist+1, visited)
        if res_temp is not None:
            if res_best is None:
                res_best = res_temp
            if res_best is not None:
                res_best = max(res_temp, res_best)

        visited = visited[:-1]
    return res_best


d = {}
input_list = u.import_data('23')
start_pos = (1, 1)
end_pos = (len(input_list)-2, len(input_list[0])-2)
visited_init = [start_pos]
final_dist = walk_dfs(start_pos, input_list, 2, visited_init)
print(final_dist)
